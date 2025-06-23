#!/usr/bin/env python
"""すべての知識データを統合して読み込むスクリプト

プログラミング言語、アルゴリズム、デザインパターンなど、
すべての知識データを統合してknowledge_base.jsonに保存します。
"""

from pathlib import Path
from star_tactics.models import KnowledgeBase
from star_tactics.storage import JSONStorage

# 各データモジュールをインポート
from programming_knowledge import create_programming_languages_data, create_frameworks_data, create_tools_data, create_relationships
from algorithms_data import load_algorithms_data
from design_patterns_data import load_design_patterns_data
from database_data import create_database_data, create_database_relationships
from cloud_infrastructure_data import create_cloud_infrastructure_data, create_cloud_infrastructure_relationships
from security_data import create_security_data, create_security_relationships
from ai_ml_data import create_ai_ml_data, create_ai_ml_relationships


def add_metadata_to_nodes(kb: KnowledgeBase):
    """ノードにメタデータを追加（可視化用）"""
    # カテゴリー別の色設定
    category_colors = {
        "プログラミング言語": "#FF6B6B",    # 赤系
        "フレームワーク": "#4ECDC4",        # 青緑系
        "開発ツール": "#45B7D1",            # 青系
        "アルゴリズム": "#96CEB4",          # 緑系
        "デザインパターン": "#DDA0DD",      # 紫系
        "データベース": "#FF8C42",          # オレンジ系
        "クラウド": "#A8E6CF",              # 薄緑系
        "セキュリティ": "#FF6B9D",          # ピンク系
        "機械学習": "#6BB6FF",              # 青系
        "深層学習": "#9B59B6",              # 紫系
        "LLM": "#F39C12",                   # 黄色系
    }
    
    # 重要度スコアの設定（仮）
    importance_scores = {
        # プログラミング言語
        "Python": 9, "JavaScript": 9, "TypeScript": 8, "Java": 8, "Go": 7, "Rust": 7,
        # フレームワーク
        "React": 9, "Django": 8, "FastAPI": 8, "Express": 7, "Vue.js": 7, "Next.js": 8,
        # 開発ツール
        "Git": 10, "Docker": 8, "Visual Studio Code": 8, "GitHub": 9, "uv": 6, "npm": 7,
        # データベース
        "MySQL": 8, "PostgreSQL": 8, "MongoDB": 7, "Redis": 7, "SQLite": 6, "Elasticsearch": 6,
        # クラウド
        "Amazon Web Services (AWS)": 9, "Microsoft Azure": 8, "Google Cloud Platform (GCP)": 8,
        "Kubernetes": 8, "Terraform": 7, "Jenkins": 7, "GitHub Actions": 8,
        # セキュリティ
        "TLS/SSL": 9, "OAuth 2.0": 8, "JSON Web Token (JWT)": 7, "OWASP": 8,
        # AI・機械学習
        "TensorFlow": 8, "PyTorch": 8, "GPT (Generative Pre-trained Transformer)": 9,
        "Claude": 7, "Pandas": 8, "NumPy": 8, "Jupyter Notebook": 7,
        # アルゴリズム
        "クイックソート": 7, "深さ優先探索 (DFS)": 8, "二分探索": 7, "ダイクストラ法": 6,
        # デザインパターン
        "Observer パターン": 8, "Singleton パターン": 7, "Strategy パターン": 7,
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
    
    # プログラミング言語とデザインパターンの関係
    if "javascript" in all_nodes and "observer" in all_nodes:
        kb.add_bidirectional_link(all_nodes["javascript"], all_nodes["observer"])
    
    if "git" in all_nodes and "iterator" in all_nodes:
        kb.add_bidirectional_link(all_nodes["git"], all_nodes["iterator"])
    
    if "react" in all_nodes and "composite" in all_nodes:
        kb.add_bidirectional_link(all_nodes["react"], all_nodes["composite"])
    
    if "python" in all_nodes and "singleton" in all_nodes:
        kb.add_bidirectional_link(all_nodes["python"], all_nodes["singleton"])
    
    if "java" in all_nodes and "factory_method" in all_nodes:
        kb.add_bidirectional_link(all_nodes["java"], all_nodes["factory_method"])
    
    # アルゴリズムとプログラミング言語の関係
    programming_languages = ["python", "javascript", "java", "go", "rust"]
    algorithms = ["quick_sort", "merge_sort", "binary_search", "dfs", "bfs"]
    
    for lang in programming_languages:
        if lang in all_nodes:
            for algo in algorithms:
                if algo in all_nodes:
                    kb.add_bidirectional_link(all_nodes[lang], all_nodes[algo])
    
    # フレームワークとデザインパターンの関係
    if "django" in all_nodes and "mvc" in all_nodes:
        kb.add_bidirectional_link(all_nodes["django"], all_nodes["mvc"])
    
    if "fastapi" in all_nodes and "singleton" in all_nodes:
        kb.add_bidirectional_link(all_nodes["fastapi"], all_nodes["singleton"])
    
    if "react" in all_nodes and "observer" in all_nodes:
        kb.add_bidirectional_link(all_nodes["react"], all_nodes["observer"])
    
    # データベースとフレームワークの関係
    databases = ["mysql", "postgresql", "mongodb", "redis"]
    frameworks = ["django", "fastapi", "express", "nextjs"]
    
    for db in databases:
        if db in all_nodes:
            for fw in frameworks:
                if fw in all_nodes:
                    kb.add_bidirectional_link(all_nodes[db], all_nodes[fw])
    
    # クラウドとツールの関係
    cloud_services = ["aws", "azure", "gcp"]
    dev_tools = ["docker", "kubernetes", "terraform", "jenkins"]
    
    for cloud in cloud_services:
        if cloud in all_nodes:
            for tool in dev_tools:
                if tool in all_nodes:
                    kb.add_bidirectional_link(all_nodes[cloud], all_nodes[tool])
    
    # セキュリティとフレームワークの関係
    security_concepts = ["oauth2", "jwt", "tls", "xss", "csrf"]
    web_frameworks = ["django", "fastapi", "express", "react", "nextjs"]
    
    for sec in security_concepts:
        if sec in all_nodes:
            for fw in web_frameworks:
                if fw in all_nodes:
                    kb.add_bidirectional_link(all_nodes[sec], all_nodes[fw])


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
    
    # データベースの読み込み
    print("\n4. データベースデータを読み込み中...")
    databases = create_database_data(kb)
    all_nodes.update(databases)
    
    # クラウド・インフラの読み込み
    print("\n5. クラウド・インフラデータを読み込み中...")
    cloud_infra = create_cloud_infrastructure_data(kb)
    all_nodes.update(cloud_infra)
    
    # セキュリティの読み込み
    print("\n6. セキュリティデータを読み込み中...")
    security = create_security_data(kb)
    all_nodes.update(security)
    
    # AI・機械学習の読み込み
    print("\n7. AI・機械学習データを読み込み中...")
    ai_ml = create_ai_ml_data(kb)
    all_nodes.update(ai_ml)
    
    # カテゴリー間の関係性を作成
    print("\n8. カテゴリー間の関係性を構築中...")
    create_cross_category_relationships(kb, all_nodes)
    
    # 追加の関係性を作成
    create_relationships(kb, all_nodes)  # プログラミング知識の関係性
    create_database_relationships(kb, all_nodes)
    create_cloud_infrastructure_relationships(kb, all_nodes)
    create_security_relationships(kb, all_nodes)
    create_ai_ml_relationships(kb, all_nodes)
    
    # メタデータを追加
    print("\n9. 可視化用メタデータを追加中...")
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