#!/usr/bin/env python
"""すべての知識データを統合して読み込むスクリプト

プログラミング言語、アルゴリズム、デザインパターンなど、
すべての知識データを統合してknowledge_base.jsonに保存します。
"""

from pathlib import Path
from star_tactics.models import KnowledgeBase
from star_tactics.storage import JSONStorage

# 各データモジュールをインポート
from programming_knowledge import create_programming_languages_data, create_frameworks_data, create_tools_data
from algorithms_data import load_algorithms_data
from design_patterns_data import load_design_patterns_data


def add_metadata_to_nodes(kb: KnowledgeBase):
    """ノードにメタデータを追加（可視化用）"""
    # カテゴリー別の色設定
    category_colors = {
        "プログラミング言語": "#FF6B6B",    # 赤系
        "フレームワーク": "#4ECDC4",        # 青緑系
        "開発ツール": "#45B7D1",            # 青系
        "アルゴリズム": "#96CEB4",          # 緑系
        "デザインパターン": "#DDA0DD",      # 紫系
    }
    
    # 重要度スコアの設定（仮）
    importance_scores = {
        "Python": 9,
        "JavaScript": 9,
        "TypeScript": 8,
        "React": 9,
        "Git": 10,
        "Docker": 8,
        "Observer パターン": 8,
        "クイックソート": 7,
        "深さ優先探索 (DFS)": 8,
    }
    
    # 各ノードにメタデータを追加
    for node in kb.get_all_nodes():
        # カテゴリーを特定
        category = None
        for tag in node.tags:
            if tag in category_colors:
                category = tag
                break
        
        # メタデータを設定（本来はノードの属性として持つべきだが、デモ用に簡易実装）
        node.metadata = {
            "category": category,
            "color": category_colors.get(category, "#999999"),
            "importance": importance_scores.get(node.title, 5),
            "connections": len(node.links)
        }


def create_cross_category_relationships(kb: KnowledgeBase, all_nodes: dict):
    """カテゴリーをまたがる関係性を作成"""
    # Python - Django - MVC パターンの関係
    if "python" in all_nodes and "django" in all_nodes:
        # すでにリンクされているはず
        pass
    
    # JavaScript - Observer パターン（イベント駆動）
    if "javascript" in all_nodes and "observer" in all_nodes:
        kb.add_bidirectional_link(all_nodes["javascript"], all_nodes["observer"])
    
    # Git - Iterator パターン（コミット履歴の走査）
    if "git" in all_nodes and "iterator" in all_nodes:
        kb.add_bidirectional_link(all_nodes["git"], all_nodes["iterator"])
    
    # React - Composite パターン（コンポーネントツリー）
    if "react" in all_nodes and "composite" in all_nodes:
        kb.add_bidirectional_link(all_nodes["react"], all_nodes["composite"])
    
    # アルゴリズムとプログラミング言語の関係
    if "python" in all_nodes and "quick_sort" in all_nodes:
        kb.add_bidirectional_link(all_nodes["python"], all_nodes["quick_sort"])


def main():
    """メイン処理"""
    # ストレージの初期化
    data_file = Path("knowledge_base.json")
    storage = JSONStorage(data_file)
    kb = KnowledgeBase(storage=storage)
    
    print("="*60)
    print("星空戦術室 - 知識データベース構築")
    print("="*60)
    
    # 既存データをクリア（開発中のため）
    for node in kb.get_all_nodes():
        kb.delete_node(node.id)
    
    # すべてのノードを格納する辞書
    all_nodes = {}
    
    # プログラミング知識の読み込み
    print("\n1. プログラミング知識を読み込み中...")
    languages = create_programming_languages_data(kb)
    all_nodes.update(languages)
    frameworks = create_frameworks_data(kb)
    all_nodes.update(frameworks)
    tools = create_tools_data(kb)
    all_nodes.update(tools)
    
    # アルゴリズムの読み込み
    print("\n2. アルゴリズムデータを読み込み中...")
    algorithms = load_algorithms_data(kb)
    all_nodes.update(algorithms)
    
    # デザインパターンの読み込み
    print("\n3. デザインパターンデータを読み込み中...")
    patterns = load_design_patterns_data(kb)
    all_nodes.update(patterns)
    
    # カテゴリー間の関係性を作成
    print("\n4. カテゴリー間の関係性を構築中...")
    create_cross_category_relationships(kb, all_nodes)
    
    # メタデータを追加
    print("\n5. 可視化用メタデータを追加中...")
    add_metadata_to_nodes(kb)
    
    # 統計情報の表示
    print("\n" + "="*60)
    print("データ構築完了！")
    print("="*60)
    
    nodes = kb.get_all_nodes()
    total_nodes = len(nodes)
    total_links = sum(len(node.links) for node in nodes)
    
    # カテゴリー別統計
    category_stats = {}
    for node in nodes:
        for tag in node.tags:
            if tag in ["プログラミング言語", "フレームワーク", "開発ツール", "アルゴリズム", "デザインパターン"]:
                category_stats[tag] = category_stats.get(tag, 0) + 1
                break
    
    print(f"\n総ノード数: {total_nodes}")
    print(f"総リンク数: {total_links}")
    print(f"平均リンク数: {total_links / total_nodes:.1f}")
    
    print("\nカテゴリー別ノード数:")
    for category, count in sorted(category_stats.items()):
        print(f"  - {category}: {count}")
    
    print(f"\nデータは {data_file} に保存されました。")
    print("\nこのデータを使って、知識の銀河を可視化しましょう！✨")


if __name__ == "__main__":
    main()