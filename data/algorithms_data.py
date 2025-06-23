#!/usr/bin/env python
"""アルゴリズム知識データの定義

ソート、探索、グラフ理論などの基本的なアルゴリズムの知識を定義します。
"""

from typing import Dict
from star_tactics.models import KnowledgeBase


def create_sorting_algorithms(kb: KnowledgeBase) -> Dict[str, str]:
    """ソートアルゴリズムの知識ノードを作成"""
    nodes = {}
    
    # バブルソート
    nodes["bubble_sort"] = kb.create_node(
        title="バブルソート",
        content="隣接する要素を比較して交換を繰り返すシンプルなソートアルゴリズム。計算量はO(n²)で効率は良くないが、実装が簡単で理解しやすい。",
        tags=["アルゴリズム", "ソート", "比較ソート", "安定ソート", "O(n²)"]
    )
    
    # クイックソート
    nodes["quick_sort"] = kb.create_node(
        title="クイックソート",
        content="分割統治法を用いた高速なソートアルゴリズム。平均計算量O(n log n)だが、最悪の場合O(n²)。実用上最も使われるソートの一つ。",
        tags=["アルゴリズム", "ソート", "分割統治", "不安定ソート", "O(n log n)"]
    )
    
    # マージソート
    nodes["merge_sort"] = kb.create_node(
        title="マージソート",
        content="分割統治法を用いた安定なソートアルゴリズム。常にO(n log n)の計算量を保証。メモリ使用量が多いが、安定性が必要な場合に有用。",
        tags=["アルゴリズム", "ソート", "分割統治", "安定ソート", "O(n log n)"]
    )
    
    # ヒープソート
    nodes["heap_sort"] = kb.create_node(
        title="ヒープソート",
        content="ヒープ構造を利用したソートアルゴリズム。常にO(n log n)の計算量で、追加メモリを必要としない。",
        tags=["アルゴリズム", "ソート", "ヒープ", "不安定ソート", "O(n log n)"]
    )
    
    return nodes


def create_search_algorithms(kb: KnowledgeBase) -> Dict[str, str]:
    """探索アルゴリズムの知識ノードを作成"""
    nodes = {}
    
    # 線形探索
    nodes["linear_search"] = kb.create_node(
        title="線形探索",
        content="先頭から順番に要素を確認していく最も基本的な探索アルゴリズム。計算量はO(n)。ソートされていないデータに対して使用。",
        tags=["アルゴリズム", "探索", "順次探索", "O(n)"]
    )
    
    # 二分探索
    nodes["binary_search"] = kb.create_node(
        title="二分探索",
        content="ソート済み配列に対して、中央値と比較しながら探索範囲を半分ずつ絞り込む効率的な探索。計算量はO(log n)。",
        tags=["アルゴリズム", "探索", "分割統治", "O(log n)", "ソート済み"]
    )
    
    # 深さ優先探索（DFS）
    nodes["dfs"] = kb.create_node(
        title="深さ優先探索 (DFS)",
        content="グラフや木構造を探索するアルゴリズム。できるだけ深く進んでから戻る。スタックまたは再帰で実装。迷路探索などに使用。",
        tags=["アルゴリズム", "探索", "グラフ", "木構造", "スタック"]
    )
    
    # 幅優先探索（BFS）
    nodes["bfs"] = kb.create_node(
        title="幅優先探索 (BFS)",
        content="グラフや木構造を探索するアルゴリズム。同じ深さのノードを全て探索してから次の深さへ。キューで実装。最短経路探索に有用。",
        tags=["アルゴリズム", "探索", "グラフ", "木構造", "キュー", "最短経路"]
    )
    
    return nodes


def create_graph_algorithms(kb: KnowledgeBase) -> Dict[str, str]:
    """グラフアルゴリズムの知識ノードを作成"""
    nodes = {}
    
    # ダイクストラ法
    nodes["dijkstra"] = kb.create_node(
        title="ダイクストラ法",
        content="重み付きグラフの最短経路を求めるアルゴリズム。負の重みがない場合に使用。優先度付きキューを使った実装でO((V+E)log V)。",
        tags=["アルゴリズム", "グラフ", "最短経路", "貪欲法", "優先度付きキュー"]
    )
    
    # ベルマン・フォード法
    nodes["bellman_ford"] = kb.create_node(
        title="ベルマン・フォード法",
        content="負の重みを含むグラフでも最短経路を求められるアルゴリズム。計算量はO(VE)でダイクストラ法より遅いが、より汎用的。",
        tags=["アルゴリズム", "グラフ", "最短経路", "動的計画法", "負の重み"]
    )
    
    # プリム法
    nodes["prim"] = kb.create_node(
        title="プリム法",
        content="最小全域木を求める貪欲アルゴリズム。頂点を一つずつ追加しながら最小コストの辺を選択。密なグラフに適している。",
        tags=["アルゴリズム", "グラフ", "最小全域木", "貪欲法"]
    )
    
    # クラスカル法
    nodes["kruskal"] = kb.create_node(
        title="クラスカル法",
        content="最小全域木を求める貪欲アルゴリズム。全ての辺をコスト順にソートし、閉路を作らない辺を選択。疎なグラフに適している。",
        tags=["アルゴリズム", "グラフ", "最小全域木", "貪欲法", "Union-Find"]
    )
    
    return nodes


def create_dynamic_programming(kb: KnowledgeBase) -> Dict[str, str]:
    """動的計画法の知識ノードを作成"""
    nodes = {}
    
    # フィボナッチ数列
    nodes["fibonacci"] = kb.create_node(
        title="フィボナッチ数列（動的計画法）",
        content="メモ化や表を使って効率的にフィボナッチ数を計算。単純な再帰のO(2^n)からO(n)に改善。動的計画法の入門例。",
        tags=["アルゴリズム", "動的計画法", "メモ化", "最適化"]
    )
    
    # ナップサック問題
    nodes["knapsack"] = kb.create_node(
        title="ナップサック問題",
        content="限られた容量のナップサックに、価値の総和が最大となるように品物を選ぶ問題。0-1ナップサックは動的計画法の典型例。",
        tags=["アルゴリズム", "動的計画法", "最適化問題", "組み合わせ"]
    )
    
    # 最長共通部分列（LCS）
    nodes["lcs"] = kb.create_node(
        title="最長共通部分列 (LCS)",
        content="2つの文字列から共通する最長の部分列を見つける問題。動的計画法により効率的に解ける。diff コマンドなどで使用。",
        tags=["アルゴリズム", "動的計画法", "文字列", "部分列"]
    )
    
    return nodes


def create_algorithm_relationships(kb: KnowledgeBase, all_nodes: Dict[str, str]):
    """アルゴリズム間の関係性を作成"""
    # ソートアルゴリズム間の関係
    if "quick_sort" in all_nodes and "merge_sort" in all_nodes:
        kb.add_bidirectional_link(all_nodes["quick_sort"], all_nodes["merge_sort"])  # 分割統治仲間
    
    # 探索アルゴリズムの関係
    if "dfs" in all_nodes and "bfs" in all_nodes:
        kb.add_bidirectional_link(all_nodes["dfs"], all_nodes["bfs"])  # グラフ探索仲間
    
    # グラフアルゴリズムの関係
    if "dijkstra" in all_nodes and "bellman_ford" in all_nodes:
        kb.add_bidirectional_link(all_nodes["dijkstra"], all_nodes["bellman_ford"])  # 最短経路仲間
    
    if "prim" in all_nodes and "kruskal" in all_nodes:
        kb.add_bidirectional_link(all_nodes["prim"], all_nodes["kruskal"])  # 最小全域木仲間
    
    # プログラミング言語との関係（もし存在すれば）
    # これは programming_knowledge.py で作成したノードとリンクできる


def load_algorithms_data(kb: KnowledgeBase) -> Dict[str, str]:
    """アルゴリズムデータを読み込む"""
    all_nodes = {}
    
    print("アルゴリズムデータを追加中...")
    
    # 各カテゴリーのアルゴリズムを作成
    sorting_nodes = create_sorting_algorithms(kb)
    all_nodes.update(sorting_nodes)
    
    search_nodes = create_search_algorithms(kb)
    all_nodes.update(search_nodes)
    
    graph_nodes = create_graph_algorithms(kb)
    all_nodes.update(graph_nodes)
    
    dp_nodes = create_dynamic_programming(kb)
    all_nodes.update(dp_nodes)
    
    # 関係性を作成
    create_algorithm_relationships(kb, all_nodes)
    
    return all_nodes