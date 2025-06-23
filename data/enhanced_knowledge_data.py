#!/usr/bin/env python
"""拡張版知識データの定義

正確な情報源に基づいた知識データと、可視化用のメタデータを含みます。
"""

from typing import Dict, Any
from star_tactics.models import KnowledgeBase


# 正確な作成年データ
CREATION_YEARS = {
    "Python": 1991,
    "JavaScript": 1995,
    "TypeScript": 2012,
    "Rust": 2015,  # 1.0 stable release
    "Go": 2012,     # 1.0 release
    "Java": 1995,
    "React": 2013,
    "Vue.js": 2014,
    "Django": 2005,
    "FastAPI": 2018,
    "Git": 2005,
    "Docker": 2013,
}

# 重要度スコア（1-10）- Stack Overflow調査、GitHub人気度などに基づく
IMPORTANCE_SCORES = {
    "Python": 10,
    "JavaScript": 10,
    "TypeScript": 8,
    "Rust": 7,
    "Go": 7,
    "Java": 9,
    "React": 9,
    "Vue.js": 8,
    "Django": 7,
    "FastAPI": 6,
    "Git": 10,
    "Docker": 9,
}

# 学習難易度（1-10）
DIFFICULTY_LEVELS = {
    "Python": 3,      # 初心者に優しい
    "JavaScript": 4,  # 非同期処理などで複雑
    "TypeScript": 6,  # 型システムの理解が必要
    "Rust": 9,        # 所有権システムが難しい
    "Go": 5,          # シンプルだが並行処理が複雑
    "Java": 6,        # OOPとエコシステムが複雑
    "React": 6,       # 状態管理とライフサイクル
    "Vue.js": 4,      # 段階的に学習可能
    "Django": 7,      # 多機能で学習項目が多い
    "FastAPI": 5,     # Pythonを知っていれば簡単
    "Git": 5,         # 基本は簡単、高度な操作は難しい
    "Docker": 6,      # コンテナ概念の理解が必要
}

# カテゴリー別の色設定（可視化用）
CATEGORY_COLORS = {
    "プログラミング言語": "#FF6B6B",    # 赤系
    "フレームワーク": "#4ECDC4",        # 青緑系
    "開発ツール": "#45B7D1",            # 青系
    "アルゴリズム": "#96CEB4",          # 緑系
    "デザインパターン": "#DDA0DD",      # 紫系
}


def create_enhanced_programming_languages(kb: KnowledgeBase) -> Dict[str, str]:
    """正確な情報に基づいたプログラミング言語ノードを作成"""
    nodes = {}
    
    # Python - 公式ドキュメントより
    nodes["python"] = kb.create_node(
        title="Python",
        content="効率的な高レベルデータ構造とシンプルだが効果的なオブジェクト指向プログラミングのアプローチを持つ、習得しやすく強力なプログラミング言語。1991年にGuido van Rossumによって作成。",
        tags=["プログラミング言語", "動的型付け", "インタープリタ", "オープンソース"],
        metadata={
            "created_year": 1991,
            "importance": 10,
            "difficulty": 3,
            "creator": "Guido van Rossum",
            "category": "プログラミング言語",
            "color": CATEGORY_COLORS["プログラミング言語"]
        }
    )
    
    # JavaScript - 公式資料より
    nodes["javascript"] = kb.create_node(
        title="JavaScript",
        content="1995年にBrendan Eichによって2週間で作られた、Web開発の中心的言語。Netscape Navigator向けに開発され、現在はブラウザとNode.jsで動作。",
        tags=["プログラミング言語", "動的型付け", "インタープリタ", "Web"],
        metadata={
            "created_year": 1995,
            "importance": 10,
            "difficulty": 4,
            "creator": "Brendan Eich",
            "category": "プログラミング言語",
            "color": CATEGORY_COLORS["プログラミング言語"]
        }
    )
    
    # TypeScript - Microsoft公式より
    nodes["typescript"] = kb.create_node(
        title="TypeScript",
        content="2012年にMicrosoftのAnders Hejlsberg（C#の設計者）によって発表されたJavaScriptのスーパーセット。静的型付けとモダンな機能を追加。",
        tags=["プログラミング言語", "静的型付け", "トランスパイル", "Web", "Microsoft"],
        metadata={
            "created_year": 2012,
            "importance": 8,
            "difficulty": 6,
            "creator": "Anders Hejlsberg",
            "category": "プログラミング言語",
            "color": CATEGORY_COLORS["プログラミング言語"]
        }
    )
    
    # Rust - 公式資料より
    nodes["rust"] = kb.create_node(
        title="Rust",
        content="2006年にGraydon Hoareが個人プロジェクトとして開始、2009年にMozillaがスポンサーになり、2015年に1.0安定版リリース。メモリ安全性とパフォーマンスを両立。",
        tags=["プログラミング言語", "静的型付け", "コンパイル", "システム", "メモリ安全"],
        metadata={
            "created_year": 2015,
            "importance": 7,
            "difficulty": 9,
            "creator": "Graydon Hoare",
            "category": "プログラミング言語",
            "color": CATEGORY_COLORS["プログラミング言語"]
        }
    )
    
    # Go - 公式資料より
    nodes["go"] = kb.create_node(
        title="Go",
        content="2007年にGoogleのRobert Griesemer、Rob Pike、Ken Thompsonによって設計。2009年に公開、2012年に1.0リリース。シンプルさと並行処理を重視。",
        tags=["プログラミング言語", "静的型付け", "コンパイル", "並行処理", "Google"],
        metadata={
            "created_year": 2012,
            "importance": 7,
            "difficulty": 5,
            "creators": "Griesemer, Pike, Thompson",
            "category": "プログラミング言語",
            "color": CATEGORY_COLORS["プログラミング言語"]
        }
    )
    
    # Java - 公式資料より
    nodes["java"] = kb.create_node(
        title="Java",
        content="1995年にSun MicrosystemsのJames Goslingらによって開発。「一度書けばどこでも動く」の理念でプラットフォーム独立性を実現。",
        tags=["プログラミング言語", "静的型付け", "コンパイル", "JVM", "エンタープライズ"],
        metadata={
            "created_year": 1995,
            "importance": 9,
            "difficulty": 6,
            "creator": "James Gosling",
            "category": "プログラミング言語",
            "color": CATEGORY_COLORS["プログラミング言語"]
        }
    )
    
    return nodes


def create_enhanced_frameworks(kb: KnowledgeBase) -> Dict[str, str]:
    """正確な情報に基づいたフレームワークノードを作成"""
    nodes = {}
    
    # React - 公式ドキュメントより
    nodes["react"] = kb.create_node(
        title="React",
        content="仮想DOM（VDOM）を使用してUIを効率的に更新するコンポーネントベースのJavaScriptライブラリ。2013年にFacebook（現Meta）が公開。宣言的APIにより、UIの状態管理を簡潔に記述可能。",
        tags=["フレームワーク", "フロントエンド", "JavaScript", "UI", "Meta"],
        metadata={
            "created_year": 2013,
            "importance": 9,
            "difficulty": 6,
            "creator": "Facebook",
            "category": "フレームワーク",
            "color": CATEGORY_COLORS["フレームワーク"]
        }
    )
    
    # 他のフレームワークも同様に正確な情報で更新...
    
    return nodes


def add_node_metadata(node, title: str) -> None:
    """既存ノードにメタデータを追加（互換性のため）"""
    if not hasattr(node, 'metadata'):
        node.metadata = {}
    
    # デフォルト値を設定
    node.metadata.update({
        "created_year": CREATION_YEARS.get(title, 2000),
        "importance": IMPORTANCE_SCORES.get(title, 5),
        "difficulty": DIFFICULTY_LEVELS.get(title, 5),
        "connections": len(node.links)
    })
    
    # カテゴリーと色を設定
    for tag in node.tags:
        if tag in CATEGORY_COLORS:
            node.metadata["category"] = tag
            node.metadata["color"] = CATEGORY_COLORS[tag]
            break