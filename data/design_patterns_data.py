#!/usr/bin/env python
"""デザインパターン知識データの定義

GoFデザインパターンを中心に、ソフトウェア設計の知識を定義します。
"""

from typing import Dict
from star_tactics.models import KnowledgeBase


def create_creational_patterns(kb: KnowledgeBase) -> Dict[str, str]:
    """生成に関するパターンの知識ノードを作成"""
    nodes = {}
    
    # Singleton
    nodes["singleton"] = kb.create_node(
        title="Singleton パターン",
        content="クラスのインスタンスが1つしか生成されないことを保証するパターン。グローバルなアクセスポイントを提供。データベース接続やログ管理などで使用。",
        tags=["デザインパターン", "生成", "GoF", "インスタンス制御"]
    )
    
    # Factory Method
    nodes["factory_method"] = kb.create_node(
        title="Factory Method パターン",
        content="オブジェクトの生成をサブクラスに委譲するパターン。生成するオブジェクトの型を実行時に決定できる。拡張性の高い設計を実現。",
        tags=["デザインパターン", "生成", "GoF", "多態性", "拡張性"]
    )
    
    # Abstract Factory
    nodes["abstract_factory"] = kb.create_node(
        title="Abstract Factory パターン",
        content="関連する一連のオブジェクトを生成するためのインターフェースを提供。プロダクトファミリーを扱う際に有用。",
        tags=["デザインパターン", "生成", "GoF", "ファミリー", "抽象化"]
    )
    
    # Builder
    nodes["builder"] = kb.create_node(
        title="Builder パターン",
        content="複雑なオブジェクトの構築過程を隠蔽し、同じ構築過程で異なる表現を作成可能にする。段階的な構築が特徴。",
        tags=["デザインパターン", "生成", "GoF", "段階的構築", "複雑性"]
    )
    
    # Prototype
    nodes["prototype"] = kb.create_node(
        title="Prototype パターン",
        content="既存のインスタンスをコピーして新しいインスタンスを生成する。cloneメソッドを使用。生成コストが高いオブジェクトに有効。",
        tags=["デザインパターン", "生成", "GoF", "複製", "クローン"]
    )
    
    return nodes


def create_structural_patterns(kb: KnowledgeBase) -> Dict[str, str]:
    """構造に関するパターンの知識ノードを作成"""
    nodes = {}
    
    # Adapter
    nodes["adapter"] = kb.create_node(
        title="Adapter パターン",
        content="既存のクラスのインターフェースを別のインターフェースに変換。互換性のないインターフェース間の橋渡し役。",
        tags=["デザインパターン", "構造", "GoF", "変換", "互換性"]
    )
    
    # Decorator
    nodes["decorator"] = kb.create_node(
        title="Decorator パターン",
        content="オブジェクトに動的に新しい責任を追加。継承を使わずに機能拡張を実現。入出力ストリームなどで使用。",
        tags=["デザインパターン", "構造", "GoF", "動的拡張", "ラッパー"]
    )
    
    # Facade
    nodes["facade"] = kb.create_node(
        title="Facade パターン",
        content="複雑なサブシステムに対して単純化されたインターフェースを提供。クライアントとサブシステムの結合度を下げる。",
        tags=["デザインパターン", "構造", "GoF", "単純化", "統一インターフェース"]
    )
    
    # Proxy
    nodes["proxy"] = kb.create_node(
        title="Proxy パターン",
        content="別のオブジェクトへのアクセスを制御する代理オブジェクトを提供。遅延初期化、アクセス制御、リモートプロキシなどで使用。",
        tags=["デザインパターン", "構造", "GoF", "代理", "アクセス制御"]
    )
    
    # Composite
    nodes["composite"] = kb.create_node(
        title="Composite パターン",
        content="オブジェクトを木構造に組み立て、個々のオブジェクトと複合オブジェクトを同一視。ファイルシステムやUIコンポーネントで使用。",
        tags=["デザインパターン", "構造", "GoF", "木構造", "再帰的構造"]
    )
    
    return nodes


def create_behavioral_patterns(kb: KnowledgeBase) -> Dict[str, str]:
    """振る舞いに関するパターンの知識ノードを作成"""
    nodes = {}
    
    # Observer
    nodes["observer"] = kb.create_node(
        title="Observer パターン",
        content="オブジェクトの状態変化を複数のオブジェクトに通知する仕組み。イベント駆動プログラミングの基礎。MVC アーキテクチャでも使用。",
        tags=["デザインパターン", "振る舞い", "GoF", "通知", "イベント駆動"]
    )
    
    # Strategy
    nodes["strategy"] = kb.create_node(
        title="Strategy パターン",
        content="アルゴリズムをカプセル化し、実行時に切り替え可能にする。条件分岐を減らし、拡張性を高める。",
        tags=["デザインパターン", "振る舞い", "GoF", "アルゴリズム", "切り替え"]
    )
    
    # Iterator
    nodes["iterator"] = kb.create_node(
        title="Iterator パターン",
        content="集合オブジェクトの要素に順次アクセスする方法を提供。内部構造を隠蔽しながら要素を走査。",
        tags=["デザインパターン", "振る舞い", "GoF", "走査", "コレクション"]
    )
    
    # Template Method
    nodes["template_method"] = kb.create_node(
        title="Template Method パターン",
        content="アルゴリズムの骨組みを定義し、具体的な処理をサブクラスに委譲。共通処理と個別処理を分離。",
        tags=["デザインパターン", "振る舞い", "GoF", "テンプレート", "継承"]
    )
    
    # Command
    nodes["command"] = kb.create_node(
        title="Command パターン",
        content="要求をオブジェクトとしてカプセル化。要求の送信者と受信者を分離し、取り消し機能なども実現可能。",
        tags=["デザインパターン", "振る舞い", "GoF", "カプセル化", "取り消し"]
    )
    
    return nodes


def create_pattern_relationships(kb: KnowledgeBase, all_nodes: Dict[str, str]):
    """デザインパターン間の関係性を作成"""
    # Factory系の関係
    if "factory_method" in all_nodes and "abstract_factory" in all_nodes:
        kb.add_bidirectional_link(all_nodes["factory_method"], all_nodes["abstract_factory"])
    
    # Decorator と Proxy の関係（構造的に類似）
    if "decorator" in all_nodes and "proxy" in all_nodes:
        kb.add_bidirectional_link(all_nodes["decorator"], all_nodes["proxy"])
    
    # Observer と MVC の関係（もし MVC データがあれば）
    # Template Method と Strategy の関係（アルゴリズムの扱い）
    if "template_method" in all_nodes and "strategy" in all_nodes:
        kb.add_bidirectional_link(all_nodes["template_method"], all_nodes["strategy"])


def load_design_patterns_data(kb: KnowledgeBase) -> Dict[str, str]:
    """デザインパターンデータを読み込む"""
    all_nodes = {}
    
    print("デザインパターンデータを追加中...")
    
    # 各カテゴリーのパターンを作成
    creational_nodes = create_creational_patterns(kb)
    all_nodes.update(creational_nodes)
    
    structural_nodes = create_structural_patterns(kb)
    all_nodes.update(structural_nodes)
    
    behavioral_nodes = create_behavioral_patterns(kb)
    all_nodes.update(behavioral_nodes)
    
    # 関係性を作成
    create_pattern_relationships(kb, all_nodes)
    
    return all_nodes