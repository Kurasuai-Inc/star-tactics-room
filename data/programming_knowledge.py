#!/usr/bin/env python
"""プログラミング知識データの定義

星空戦術室に登録する実際の知識データを定義します。
カテゴリー別に整理し、関連性も含めてデータ化します。
"""

from typing import Dict, List, Tuple
from star_tactics.models import KnowledgeBase
from star_tactics.storage import JSONStorage


# リンクの関係性タイプ
LINK_TYPES = {
    "USES": "使用する",
    "DERIVED": "派生",
    "COMPETES": "競合",
    "COMPLEMENTS": "補完", 
    "IMPLEMENTS": "実装",
    "DEPENDS": "依存",
    "SIMILAR": "類似",
}


def create_programming_languages_data(kb: KnowledgeBase) -> Dict[str, str]:
    """プログラミング言語の知識ノードを作成"""
    nodes = {}
    
    # Python
    nodes["python"] = kb.create_node(
        title="Python",
        content="高レベル汎用プログラミング言語。読みやすく書きやすい文法が特徴。データサイエンス、Web開発、自動化など幅広い用途で使用される。",
        tags=["プログラミング言語", "動的型付け", "インタープリタ", "オープンソース"]
    )
    
    # JavaScript
    nodes["javascript"] = kb.create_node(
        title="JavaScript", 
        content="Web開発の中心的な言語。ブラウザ上で動作し、Node.jsによりサーバーサイドでも使用可能。非同期処理やイベント駆動が特徴。",
        tags=["プログラミング言語", "動的型付け", "インタープリタ", "Web"]
    )
    
    # TypeScript
    nodes["typescript"] = kb.create_node(
        title="TypeScript",
        content="JavaScriptに静的型付けを追加した言語。大規模アプリケーション開発に適しており、型安全性とIDEサポートが強力。",
        tags=["プログラミング言語", "静的型付け", "トランスパイル", "Web", "Microsoft"]
    )
    
    # Rust
    nodes["rust"] = kb.create_node(
        title="Rust",
        content="メモリ安全性とパフォーマンスを両立したシステムプログラミング言語。所有権システムによりメモリ管理を自動化。",
        tags=["プログラミング言語", "静的型付け", "コンパイル", "システム", "メモリ安全"]
    )
    
    # Go
    nodes["go"] = kb.create_node(
        title="Go",
        content="Googleが開発したシンプルで高速なプログラミング言語。並行処理のサポートが組み込まれており、クラウドネイティブ開発に人気。",
        tags=["プログラミング言語", "静的型付け", "コンパイル", "並行処理", "Google"]
    )
    
    # Java
    nodes["java"] = kb.create_node(
        title="Java",
        content="プラットフォーム独立性を持つオブジェクト指向言語。エンタープライズアプリケーションやAndroid開発で広く使用される。",
        tags=["プログラミング言語", "静的型付け", "コンパイル", "JVM", "エンタープライズ"]
    )
    
    return nodes


def create_frameworks_data(kb: KnowledgeBase) -> Dict[str, str]:
    """フレームワークの知識ノードを作成"""
    nodes = {}
    
    # React
    nodes["react"] = kb.create_node(
        title="React",
        content="FacebookとMetaが開発したUIライブラリ。仮想DOMとコンポーネントベースの設計により、効率的なUI開発が可能。",
        tags=["フレームワーク", "フロントエンド", "JavaScript", "UI", "Meta"]
    )
    
    # Vue.js
    nodes["vue"] = kb.create_node(
        title="Vue.js",
        content="プログレッシブJavaScriptフレームワーク。段階的に採用でき、学習曲線が緩やか。リアクティブなデータバインディングが特徴。",
        tags=["フレームワーク", "フロントエンド", "JavaScript", "UI", "プログレッシブ"]
    )
    
    # FastAPI
    nodes["fastapi"] = kb.create_node(
        title="FastAPI",
        content="高速で現代的なPython WebフレームワークAPI。自動ドキュメント生成、型ヒントベースのバリデーション、非同期サポートが特徴。",
        tags=["フレームワーク", "バックエンド", "Python", "API", "非同期"]
    )
    
    # Django
    nodes["django"] = kb.create_node(
        title="Django",
        content="Pythonの高機能Webフレームワーク。「バッテリー同梱」の哲学で、認証、管理画面、ORMなど多くの機能を標準搭載。",
        tags=["フレームワーク", "バックエンド", "Python", "フルスタック", "MVC"]
    )
    
    # Next.js
    nodes["nextjs"] = kb.create_node(
        title="Next.js",
        content="Reactベースのフルスタックフレームワーク。SSR、SSG、APIルートなどを提供し、プロダクション対応のWebアプリを構築可能。",
        tags=["フレームワーク", "フルスタック", "React", "JavaScript", "Vercel"]
    )
    
    # Express
    nodes["express"] = kb.create_node(
        title="Express",
        content="Node.js向けの最小限で柔軟なWebアプリケーションフレームワーク。シンプルなAPIで強力なWebアプリやAPIを構築。",
        tags=["フレームワーク", "バックエンド", "JavaScript", "Node.js", "最小限"]
    )
    
    return nodes


def create_tools_data(kb: KnowledgeBase) -> Dict[str, str]:
    """開発ツールの知識ノードを作成"""
    nodes = {}
    
    # Git
    nodes["git"] = kb.create_node(
        title="Git",
        content="分散型バージョン管理システム。ソースコードの変更履歴を管理し、複数人での協調開発を可能にする。",
        tags=["開発ツール", "バージョン管理", "分散型", "オープンソース"]
    )
    
    # Docker
    nodes["docker"] = kb.create_node(
        title="Docker", 
        content="コンテナ仮想化技術。アプリケーションとその依存関係をパッケージ化し、どこでも同じ環境で実行可能にする。",
        tags=["開発ツール", "コンテナ", "仮想化", "DevOps"]
    )
    
    # VSCode
    nodes["vscode"] = kb.create_node(
        title="Visual Studio Code",
        content="Microsoftが開発した軽量で強力なコードエディタ。豊富な拡張機能とIntelliSenseによる開発支援が特徴。",
        tags=["開発ツール", "エディタ", "IDE", "Microsoft", "オープンソース"]
    )
    
    # uv
    nodes["uv"] = kb.create_node(
        title="uv",
        content="Rustで書かれた高速なPythonパッケージマネージャ。pipとvenvの機能を統合し、依存関係解決が高速。",
        tags=["開発ツール", "パッケージ管理", "Python", "Rust"]
    )
    
    # GitHub
    nodes["github"] = kb.create_node(
        title="GitHub",
        content="Gitリポジトリのホスティングサービス。ソーシャルコーディング機能、PR、Issues、Actionsなどの開発支援機能を提供。",
        tags=["開発ツール", "Git", "ホスティング", "CI/CD", "Microsoft"]
    )
    
    return nodes


def create_relationships(kb: KnowledgeBase, all_nodes: Dict[str, str]):
    """ノード間の関係性を作成"""
    # TypeScript -> JavaScript (派生)
    if "typescript" in all_nodes and "javascript" in all_nodes:
        kb.add_bidirectional_link(all_nodes["typescript"], all_nodes["javascript"])
    
    # React -> JavaScript (使用)
    if "react" in all_nodes and "javascript" in all_nodes:
        kb.add_bidirectional_link(all_nodes["react"], all_nodes["javascript"])
    
    # Vue.js -> JavaScript (使用)
    if "vue" in all_nodes and "javascript" in all_nodes:
        kb.add_bidirectional_link(all_nodes["vue"], all_nodes["javascript"])
    
    # FastAPI -> Python (実装)
    if "fastapi" in all_nodes and "python" in all_nodes:
        kb.add_bidirectional_link(all_nodes["fastapi"], all_nodes["python"])
    
    # Django -> Python (実装)
    if "django" in all_nodes and "python" in all_nodes:
        kb.add_bidirectional_link(all_nodes["django"], all_nodes["python"])
    
    # Next.js -> React (使用)
    if "nextjs" in all_nodes and "react" in all_nodes:
        kb.add_bidirectional_link(all_nodes["nextjs"], all_nodes["react"])
    
    # Express -> JavaScript (実装)
    if "express" in all_nodes and "javascript" in all_nodes:
        kb.add_bidirectional_link(all_nodes["express"], all_nodes["javascript"])
    
    # React <-> Vue.js (競合)
    if "react" in all_nodes and "vue" in all_nodes:
        kb.add_bidirectional_link(all_nodes["react"], all_nodes["vue"])
    
    # FastAPI <-> Django (競合)
    if "fastapi" in all_nodes and "django" in all_nodes:
        kb.add_bidirectional_link(all_nodes["fastapi"], all_nodes["django"])
    
    # uv -> Python (関連)
    if "uv" in all_nodes and "python" in all_nodes:
        kb.add_bidirectional_link(all_nodes["uv"], all_nodes["python"])
    
    # GitHub -> Git (使用)
    if "github" in all_nodes and "git" in all_nodes:
        kb.add_bidirectional_link(all_nodes["github"], all_nodes["git"])


def load_all_knowledge_data(storage_path: str = "knowledge_base.json"):
    """すべての知識データを読み込む"""
    storage = JSONStorage(storage_path)
    kb = KnowledgeBase(storage=storage)
    
    print("プログラミング知識データを読み込み中...")
    
    # 各カテゴリーのデータを作成
    all_nodes = {}
    
    print("- プログラミング言語を追加中...")
    language_nodes = create_programming_languages_data(kb)
    all_nodes.update(language_nodes)
    
    print("- フレームワークを追加中...")
    framework_nodes = create_frameworks_data(kb)
    all_nodes.update(framework_nodes)
    
    print("- 開発ツールを追加中...")
    tools_nodes = create_tools_data(kb)
    all_nodes.update(tools_nodes)
    
    print("- 関係性を構築中...")
    create_relationships(kb, all_nodes)
    
    # 統計情報
    total_nodes = len(kb.get_all_nodes())
    total_links = sum(len(node.links) for node in kb.get_all_nodes())
    
    print(f"\n読み込み完了！")
    print(f"総ノード数: {total_nodes}")
    print(f"総リンク数: {total_links}")
    print(f"データは {storage_path} に保存されました。")
    
    return kb


if __name__ == "__main__":
    load_all_knowledge_data()