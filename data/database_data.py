#!/usr/bin/env python
"""データベース技術の知識ノードを作成"""

from typing import Dict
from star_tactics.models import KnowledgeBase


def create_database_data(kb: KnowledgeBase) -> Dict[str, str]:
    """データベース技術の知識ノードを作成"""
    nodes = {}
    
    # リレーショナルデータベース
    nodes["mysql"] = kb.create_node(
        title="MySQL",
        content="オープンソースのリレーショナルデータベース管理システム。Web アプリケーションでの使用が多く、高いパフォーマンスと信頼性を持つ。Oracle が開発・保守している。",
        tags=["データベース", "リレーショナル", "SQL", "オープンソース", "Oracle"]
    )
    
    nodes["postgresql"] = kb.create_node(
        title="PostgreSQL",
        content="高機能なオープンソース関係データベースシステム。JSON型、配列型など豊富なデータ型をサポート。ACIDコンプライアンスと拡張性が特徴。",
        tags=["データベース", "リレーショナル", "SQL", "オープンソース", "ACID"]
    )
    
    nodes["sqlite"] = kb.create_node(
        title="SQLite",
        content="軽量なファイルベースのリレーショナルデータベース。サーバー不要で組み込み用途に最適。モバイルアプリや小規模システムで広く使用される。",
        tags=["データベース", "リレーショナル", "SQL", "軽量", "組み込み"]
    )
    
    nodes["oracle"] = kb.create_node(
        title="Oracle Database",
        content="エンタープライズ向けの高機能商用データベース。大規模システムでの高い可用性とパフォーマンスを提供。多くの企業システムで採用。",
        tags=["データベース", "リレーショナル", "SQL", "商用", "エンタープライズ"]
    )
    
    # NoSQLデータベース
    nodes["mongodb"] = kb.create_node(
        title="MongoDB",
        content="ドキュメント指向NoSQLデータベース。JSONライクなBSONフォーマットでデータを格納。スキーマレスで柔軟な開発が可能。",
        tags=["データベース", "NoSQL", "ドキュメント", "スキーマレス", "JSON"]
    )
    
    nodes["redis"] = kb.create_node(
        title="Redis",
        content="インメモリキーバリューストア。高速な読み書きが可能で、キャッシュやセッション管理によく使用される。データ構造サーバーとしても機能。",
        tags=["データベース", "NoSQL", "キーバリュー", "インメモリ", "キャッシュ"]
    )
    
    nodes["elasticsearch"] = kb.create_node(
        title="Elasticsearch",
        content="分散検索・分析エンジン。大量のデータから高速な全文検索が可能。ログ分析やリアルタイム分析に使用される。",
        tags=["データベース", "検索エンジン", "分散", "全文検索", "分析"]
    )
    
    nodes["cassandra"] = kb.create_node(
        title="Apache Cassandra",
        content="分散型NoSQLデータベース。高い可用性とスケーラビリティを持つワイドカラムストア。大規模なデータ処理に適している。",
        tags=["データベース", "NoSQL", "分散", "ワイドカラム", "スケーラブル"]
    )
    
    # データウェアハウス・ビッグデータ
    nodes["snowflake"] = kb.create_node(
        title="Snowflake",
        content="クラウドネイティブなデータウェアハウス。自動スケーリングと高いパフォーマンスを提供。データ分析とビジネスインテリジェンスに最適。",
        tags=["データウェアハウス", "クラウド", "分析", "スケーリング", "BI"]
    )
    
    nodes["bigquery"] = kb.create_node(
        title="Google BigQuery",
        content="Googleのサーバーレスデータウェアハウス。大規模データセットの高速分析が可能。機械学習機能も統合されている。",
        tags=["データウェアハウス", "Google", "サーバーレス", "ビッグデータ", "機械学習"]
    )
    
    return nodes


def create_database_relationships(kb: KnowledgeBase, all_nodes: Dict[str, str]):
    """データベース技術間の関係性を作成"""
    
    # リレーショナルデータベース同士の関係
    if "mysql" in all_nodes and "postgresql" in all_nodes:
        kb.add_bidirectional_link(all_nodes["mysql"], all_nodes["postgresql"])
    
    if "sqlite" in all_nodes and "mysql" in all_nodes:
        kb.add_bidirectional_link(all_nodes["sqlite"], all_nodes["mysql"])
    
    if "oracle" in all_nodes and "postgresql" in all_nodes:
        kb.add_bidirectional_link(all_nodes["oracle"], all_nodes["postgresql"])
    
    # NoSQL同士の関係
    if "mongodb" in all_nodes and "redis" in all_nodes:
        kb.add_bidirectional_link(all_nodes["mongodb"], all_nodes["redis"])
    
    if "elasticsearch" in all_nodes and "mongodb" in all_nodes:
        kb.add_bidirectional_link(all_nodes["elasticsearch"], all_nodes["mongodb"])
    
    if "cassandra" in all_nodes and "mongodb" in all_nodes:
        kb.add_bidirectional_link(all_nodes["cassandra"], all_nodes["mongodb"])
    
    # データウェアハウス同士
    if "snowflake" in all_nodes and "bigquery" in all_nodes:
        kb.add_bidirectional_link(all_nodes["snowflake"], all_nodes["bigquery"])
    
    # プログラミング言語との関係
    if "python" in all_nodes:
        for db in ["mysql", "postgresql", "mongodb", "redis", "elasticsearch"]:
            if db in all_nodes:
                kb.add_bidirectional_link(all_nodes["python"], all_nodes[db])
    
    if "javascript" in all_nodes:
        for db in ["mysql", "mongodb", "redis", "postgresql"]:
            if db in all_nodes:
                kb.add_bidirectional_link(all_nodes["javascript"], all_nodes[db])
    
    # フレームワークとの関係
    if "django" in all_nodes:
        for db in ["mysql", "postgresql", "sqlite"]:
            if db in all_nodes:
                kb.add_bidirectional_link(all_nodes["django"], all_nodes[db])
    
    if "fastapi" in all_nodes:
        for db in ["mysql", "postgresql", "mongodb", "redis"]:
            if db in all_nodes:
                kb.add_bidirectional_link(all_nodes["fastapi"], all_nodes[db])
    
    if "express" in all_nodes:
        for db in ["mongodb", "mysql", "redis"]:
            if db in all_nodes:
                kb.add_bidirectional_link(all_nodes["express"], all_nodes[db])