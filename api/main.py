#!/usr/bin/env python
"""星空戦術室 API サーバー

star-tactics-roomのデータを提供するFastAPIサーバー。
star-constellation-viewerから呼び出されることを想定。
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from pathlib import Path
import sys
import json

# star_tacticsモジュールをインポートできるようにパスを追加
sys.path.append(str(Path(__file__).parent.parent))

from star_tactics.models import KnowledgeBase
from star_tactics.storage import JSONStorage


# Pydanticモデル
class NodeMetadata(BaseModel):
    created_year: Optional[int] = None
    importance: Optional[int] = None
    difficulty: Optional[int] = None
    creator: Optional[str] = None
    category: Optional[str] = None
    color: Optional[str] = None
    connections: Optional[int] = None


class KnowledgeNodeResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str]
    links: List[str]
    created_at: str
    updated_at: str
    metadata: Optional[NodeMetadata] = None


class LinkRelationship(BaseModel):
    source: str
    target: str
    type: str = "関連"


class GraphDataResponse(BaseModel):
    nodes: List[KnowledgeNodeResponse]
    links: List[LinkRelationship]


# FastAPIアプリケーション
app = FastAPI(
    title="星空戦術室 API",
    description="知識データベースを提供するAPI",
    version="1.0.0"
)

# CORS設定（開発環境用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では特定のオリジンのみ許可すべき
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# グローバル変数として知識ベースを保持
kb: Optional[KnowledgeBase] = None


@app.on_event("startup")
async def startup_event():
    """サーバー起動時にデータを読み込む"""
    global kb
    
    # データファイルのパスを設定
    data_file = Path(__file__).parent.parent / "knowledge_base.json"
    
    if not data_file.exists():
        # データファイルが存在しない場合は、データ生成スクリプトを実行
        print("データファイルが見つかりません。生成中...")
        from data.load_all_data import main as load_data
        load_data()
    
    # 知識ベースを初期化
    storage = JSONStorage(str(data_file))
    kb = KnowledgeBase(storage=storage)
    
    print(f"データ読み込み完了: {len(kb.get_all_nodes())}ノード")


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {
        "message": "星空戦術室 API へようこそ！",
        "endpoints": {
            "/nodes": "全ノードの取得",
            "/nodes/{node_id}": "特定ノードの取得",
            "/graph": "グラフデータの取得",
            "/search": "ノードの検索",
            "/stats": "統計情報"
        }
    }


@app.get("/nodes", response_model=List[KnowledgeNodeResponse])
async def get_all_nodes():
    """全ノードを取得"""
    if kb is None:
        raise HTTPException(status_code=500, detail="データベースが初期化されていません")
    
    nodes = kb.get_all_nodes()
    return [
        KnowledgeNodeResponse(
            id=node.id,
            title=node.title,
            content=node.content,
            tags=node.tags,
            links=node.links,
            created_at=node.created_at.isoformat(),
            updated_at=node.updated_at.isoformat(),
            metadata=NodeMetadata(**getattr(node, 'metadata', {})) if hasattr(node, 'metadata') else None
        )
        for node in nodes
    ]


@app.get("/nodes/{node_id}", response_model=KnowledgeNodeResponse)
async def get_node(node_id: str):
    """特定のノードを取得"""
    if kb is None:
        raise HTTPException(status_code=500, detail="データベースが初期化されていません")
    
    node = kb.get_node(node_id)
    if node is None:
        raise HTTPException(status_code=404, detail="ノードが見つかりません")
    
    return KnowledgeNodeResponse(
        id=node.id,
        title=node.title,
        content=node.content,
        tags=node.tags,
        links=node.links,
        created_at=node.created_at.isoformat(),
        updated_at=node.updated_at.isoformat(),
        metadata=NodeMetadata(**getattr(node, 'metadata', {})) if hasattr(node, 'metadata') else None
    )


@app.get("/graph", response_model=GraphDataResponse)
async def get_graph_data():
    """グラフ可視化用のデータを取得"""
    if kb is None:
        raise HTTPException(status_code=500, detail="データベースが初期化されていません")
    
    nodes = kb.get_all_nodes()
    links = []
    
    # リンク関係を構築
    processed_links = set()  # 重複チェック用
    for node in nodes:
        for link_id in node.links:
            # 双方向リンクの重複を避けるため、ペアをソートして追加
            link_pair = tuple(sorted([node.id, link_id]))
            if link_pair not in processed_links:
                processed_links.add(link_pair)
                links.append(LinkRelationship(
                    source=link_pair[0],
                    target=link_pair[1],
                    type="関連"
                ))
    
    return GraphDataResponse(
        nodes=[
            KnowledgeNodeResponse(
                id=node.id,
                title=node.title,
                content=node.content,
                tags=node.tags,
                links=node.links,
                created_at=node.created_at.isoformat(),
                updated_at=node.updated_at.isoformat(),
                metadata=NodeMetadata(**getattr(node, 'metadata', {})) if hasattr(node, 'metadata') else None
            )
            for node in nodes
        ],
        links=links
    )


@app.get("/search")
async def search_nodes(
    text: Optional[str] = None,
    tags: Optional[str] = None
):
    """ノードを検索"""
    if kb is None:
        raise HTTPException(status_code=500, detail="データベースが初期化されていません")
    
    if tags:
        tag_list = [tag.strip() for tag in tags.split(",")]
        nodes = kb.search_by_tags(tag_list)
    elif text:
        nodes = kb.search_by_text(text)
    else:
        nodes = kb.get_all_nodes()
    
    return [
        KnowledgeNodeResponse(
            id=node.id,
            title=node.title,
            content=node.content,
            tags=node.tags,
            links=node.links,
            created_at=node.created_at.isoformat(),
            updated_at=node.updated_at.isoformat(),
            metadata=NodeMetadata(**getattr(node, 'metadata', {})) if hasattr(node, 'metadata') else None
        )
        for node in nodes
    ]


@app.get("/stats")
async def get_stats():
    """統計情報を取得"""
    if kb is None:
        raise HTTPException(status_code=500, detail="データベースが初期化されていません")
    
    nodes = kb.get_all_nodes()
    total_nodes = len(nodes)
    total_links = sum(len(node.links) for node in nodes)
    
    # カテゴリー別統計
    category_stats = {}
    for node in nodes:
        if hasattr(node, 'metadata') and node.metadata.get('category'):
            category = node.metadata['category']
            category_stats[category] = category_stats.get(category, 0) + 1
    
    return {
        "total_nodes": total_nodes,
        "total_links": total_links,
        "average_links_per_node": total_links / total_nodes if total_nodes > 0 else 0,
        "categories": category_stats
    }


@app.get("/debug/small")
async def get_small_dataset():
    """デバッグ用小規模データセット（10ノード・5リンク）"""
    if kb is None:
        raise HTTPException(status_code=500, detail="データベースが初期化されていません")
    
    nodes = kb.get_all_nodes()[:10]  # 最初の10ノードのみ
    simple_nodes = []
    simple_links = []
    
    # シンプルなノード形式
    for node in nodes:
        simple_nodes.append({
            "id": node.id,
            "title": node.title,
            "category": getattr(node, 'metadata', {}).get('category', 'unknown') if hasattr(node, 'metadata') else 'unknown'
        })
    
    # 10ノード内でのリンクのみ抽出
    node_ids = [n.id for n in nodes]
    processed_links = set()
    
    for node in nodes:
        for link_id in node.links:
            if link_id in node_ids:
                link_pair = tuple(sorted([node.id, link_id]))
                if link_pair not in processed_links and len(simple_links) < 5:
                    processed_links.add(link_pair)
                    simple_links.append({
                        "source": link_pair[0],
                        "target": link_pair[1]
                    })
    
    return {
        "nodes": simple_nodes,
        "links": simple_links,
        "debug_info": {
            "total_available_nodes": len(kb.get_all_nodes()),
            "showing_nodes": len(simple_nodes),
            "showing_links": len(simple_links)
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)