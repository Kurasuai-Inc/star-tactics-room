#!/usr/bin/env python
"""AI・機械学習技術の知識ノードを作成"""

from typing import Dict
from star_tactics.models import KnowledgeBase


def create_ai_ml_data(kb: KnowledgeBase) -> Dict[str, str]:
    """AI・機械学習技術の知識ノードを作成"""
    nodes = {}
    
    # 機械学習ライブラリ・フレームワーク
    nodes["tensorflow"] = kb.create_node(
        title="TensorFlow",
        content="Googleが開発したオープンソース機械学習ライブラリ。深層学習から従来の機械学習まで幅広く対応。本番環境での運用にも適している。",
        tags=["機械学習", "深層学習", "Google", "Python", "オープンソース"]
    )
    
    nodes["pytorch"] = kb.create_node(
        title="PyTorch",
        content="Facebookが開発した深層学習フレームワーク。動的計算グラフにより柔軟な実装が可能。研究用途に人気が高い。",
        tags=["機械学習", "深層学習", "Facebook", "Python", "動的グラフ"]
    )
    
    nodes["scikit_learn"] = kb.create_node(
        title="scikit-learn",
        content="Pythonの機械学習ライブラリ。分類、回帰、クラスタリングなど従来の機械学習アルゴリズムを豊富に提供。初学者にも使いやすい。",
        tags=["機械学習", "Python", "分類", "回帰", "クラスタリング"]
    )
    
    nodes["keras"] = kb.create_node(
        title="Keras",
        content="高レベル深層学習API。TensorFlowのバックエンドとして統合。シンプルで直感的なインターフェースで深層学習モデルを構築可能。",
        tags=["機械学習", "深層学習", "API", "TensorFlow", "高レベル"]
    )
    
    # データ処理・分析
    nodes["pandas"] = kb.create_node(
        title="Pandas",
        content="Pythonのデータ分析ライブラリ。データフレーム操作、データクリーニング、統計処理など幅広い機能を提供。データサイエンスの必須ツール。",
        tags=["データ分析", "Python", "データフレーム", "統計", "前処理"]
    )
    
    nodes["numpy"] = kb.create_node(
        title="NumPy",
        content="Pythonの数値計算ライブラリ。多次元配列操作と数学関数を提供。多くの科学計算ライブラリの基盤となっている。",
        tags=["数値計算", "Python", "配列", "数学", "基盤ライブラリ"]
    )
    
    nodes["matplotlib"] = kb.create_node(
        title="Matplotlib",
        content="Pythonのグラフ描画ライブラリ。様々な形式のグラフ・チャートを作成可能。データ可視化の標準的なツール。",
        tags=["可視化", "Python", "グラフ", "チャート", "プロット"]
    )
    
    nodes["jupyter"] = kb.create_node(
        title="Jupyter Notebook",
        content="インタラクティブな開発環境。コード、テキスト、グラフを組み合わせたノートブック形式。データサイエンスや機械学習の実験に最適。",
        tags=["開発環境", "ノートブック", "データサイエンス", "可視化", "実験"]
    )
    
    # 深層学習・ニューラルネットワーク
    nodes["cnn"] = kb.create_node(
        title="畳み込みニューラルネットワーク (CNN)",
        content="画像認識に特化したニューラルネットワーク。畳み込み層とプーリング層により空間的特徴を抽出。コンピュータビジョンの中核技術。",
        tags=["深層学習", "画像認識", "ニューラルネットワーク", "畳み込み", "特徴抽出"]
    )
    
    nodes["rnn"] = kb.create_node(
        title="リカレントニューラルネットワーク (RNN)",
        content="時系列データ処理に適したニューラルネットワーク。過去の情報を記憶し、シーケンシャルなデータの学習が可能。",
        tags=["深層学習", "時系列", "ニューラルネットワーク", "シーケンス", "記憶"]
    )
    
    nodes["transformer"] = kb.create_node(
        title="Transformer",
        content="注意機構（Attention）に基づくニューラルネットワークアーキテクチャ。自然言語処理で革命的な成果。GPTやBERTの基盤技術。",
        tags=["深層学習", "注意機構", "自然言語処理", "GPT", "BERT"]
    )
    
    # AI・LLM
    nodes["gpt"] = kb.create_node(
        title="GPT (Generative Pre-trained Transformer)",
        content="OpenAIが開発した大規模言語モデル。テキスト生成、質問応答、コード生成など多様なタスクに対応。GPT-4は特に高い性能を示している。",
        tags=["LLM", "生成AI", "OpenAI", "テキスト生成", "汎用AI"]
    )
    
    nodes["claude"] = kb.create_node(
        title="Claude",
        content="Anthropicが開発したAIアシスタント。安全性と有用性を重視した設計。長い文脈を理解し、様々なタスクを支援。",
        tags=["LLM", "AIアシスタント", "Anthropic", "安全性", "長文脈"]
    )
    
    nodes["bert"] = kb.create_node(
        title="BERT",
        content="Googleが開発した双方向エンコーダ表現モデル。文脈を双方向から理解し、自然言語理解タスクで高い性能を発揮。",
        tags=["LLM", "自然言語理解", "Google", "双方向", "エンコーダ"]
    )
    
    # 追加の4ノード（100ノード達成のため）
    nodes["langchain"] = kb.create_node(
        title="LangChain",
        content="LLMアプリケーション開発のためのフレームワーク。複数のAIモデルを組み合わせて複雑なワークフローを構築。RAGシステム開発に人気。",
        tags=["LLM", "フレームワーク", "RAG", "Python", "AI開発"]
    )
    
    nodes["huggingface"] = kb.create_node(
        title="Hugging Face",
        content="機械学習モデルとデータセットのプラットフォーム。Transformersライブラリで事前訓練済みモデルを簡単に利用可能。",
        tags=["機械学習", "プラットフォーム", "Transformers", "モデル共有", "コミュニティ"]
    )
    
    nodes["openai_api"] = kb.create_node(
        title="OpenAI API",
        content="GPTモデルにアクセスするためのREST API。テキスト生成、チャット、コード生成、画像生成などの機能を提供。",
        tags=["LLM", "API", "OpenAI", "GPT", "テキスト生成"]
    )
    
    nodes["vector_db"] = kb.create_node(
        title="Vector Database",
        content="ベクトル埋め込みの保存と類似検索に特化したデータベース。RAGシステムやセマンティック検索で使用される。",
        tags=["データベース", "ベクトル", "埋め込み", "類似検索", "RAG"]
    )
    
    return nodes


def create_ai_ml_relationships(kb: KnowledgeBase, all_nodes: Dict[str, str]):
    """AI・機械学習技術間の関係性を作成"""
    
    # 基盤ライブラリ間の関係
    if "numpy" in all_nodes and "pandas" in all_nodes:
        kb.add_bidirectional_link(all_nodes["numpy"], all_nodes["pandas"])
    
    if "numpy" in all_nodes and "scikit_learn" in all_nodes:
        kb.add_bidirectional_link(all_nodes["numpy"], all_nodes["scikit_learn"])
    
    if "pandas" in all_nodes and "matplotlib" in all_nodes:
        kb.add_bidirectional_link(all_nodes["pandas"], all_nodes["matplotlib"])
    
    # 深層学習フレームワーク間の関係
    if "tensorflow" in all_nodes and "keras" in all_nodes:
        kb.add_bidirectional_link(all_nodes["tensorflow"], all_nodes["keras"])
    
    if "tensorflow" in all_nodes and "pytorch" in all_nodes:
        kb.add_bidirectional_link(all_nodes["tensorflow"], all_nodes["pytorch"])
    
    # ニューラルネットワーク間の関係
    if "cnn" in all_nodes and "rnn" in all_nodes:
        kb.add_bidirectional_link(all_nodes["cnn"], all_nodes["rnn"])
    
    if "transformer" in all_nodes and "rnn" in all_nodes:
        kb.add_bidirectional_link(all_nodes["transformer"], all_nodes["rnn"])
    
    # LLM間の関係
    if "gpt" in all_nodes and "transformer" in all_nodes:
        kb.add_bidirectional_link(all_nodes["gpt"], all_nodes["transformer"])
    
    if "bert" in all_nodes and "transformer" in all_nodes:
        kb.add_bidirectional_link(all_nodes["bert"], all_nodes["transformer"])
    
    if "claude" in all_nodes and "gpt" in all_nodes:
        kb.add_bidirectional_link(all_nodes["claude"], all_nodes["gpt"])
    
    # フレームワークとニューラルネットワーク
    for framework in ["tensorflow", "pytorch"]:
        if framework in all_nodes:
            for nn in ["cnn", "rnn", "transformer"]:
                if nn in all_nodes:
                    kb.add_bidirectional_link(all_nodes[framework], all_nodes[nn])
    
    # Pythonとの関係
    if "python" in all_nodes:
        for ml_tool in ["tensorflow", "pytorch", "scikit_learn", "pandas", "numpy", "matplotlib", "jupyter"]:
            if ml_tool in all_nodes:
                kb.add_bidirectional_link(all_nodes["python"], all_nodes[ml_tool])
    
    # データサイエンスワークフロー
    if "jupyter" in all_nodes:
        for tool in ["pandas", "numpy", "matplotlib", "scikit_learn", "tensorflow", "pytorch"]:
            if tool in all_nodes:
                kb.add_bidirectional_link(all_nodes["jupyter"], all_nodes[tool])
    
    # クラウドとの関係
    for cloud in ["aws", "gcp", "azure"]:
        if cloud in all_nodes:
            for ai_tool in ["tensorflow", "pytorch", "jupyter"]:
                if ai_tool in all_nodes:
                    kb.add_bidirectional_link(all_nodes[cloud], all_nodes[ai_tool])
    
    # 新規追加ノードの関係性
    if "langchain" in all_nodes:
        for related in ["openai_api", "vector_db", "python", "gpt"]:
            if related in all_nodes:
                kb.add_bidirectional_link(all_nodes["langchain"], all_nodes[related])
    
    if "huggingface" in all_nodes:
        for related in ["transformer", "bert", "pytorch", "tensorflow", "python"]:
            if related in all_nodes:
                kb.add_bidirectional_link(all_nodes["huggingface"], all_nodes[related])
    
    if "openai_api" in all_nodes:
        for related in ["gpt", "claude", "python", "javascript"]:
            if related in all_nodes:
                kb.add_bidirectional_link(all_nodes["openai_api"], all_nodes[related])
    
    if "vector_db" in all_nodes:
        for related in ["langchain", "pandas", "numpy", "elasticsearch"]:
            if related in all_nodes:
                kb.add_bidirectional_link(all_nodes["vector_db"], all_nodes[related])