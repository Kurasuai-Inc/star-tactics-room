#!/usr/bin/env python
"""クラウド・インフラ技術の知識ノードを作成"""

from typing import Dict
from star_tactics.models import KnowledgeBase


def create_cloud_infrastructure_data(kb: KnowledgeBase) -> Dict[str, str]:
    """クラウド・インフラ技術の知識ノードを作成"""
    nodes = {}
    
    # クラウドプロバイダー
    nodes["aws"] = kb.create_node(
        title="Amazon Web Services (AWS)",
        content="Amazonが提供するクラウドコンピューティングプラットフォーム。EC2、S3、Lambda など豊富なサービスを提供。世界最大のクラウドプロバイダー。",
        tags=["クラウド", "AWS", "Amazon", "インフラ", "プラットフォーム"]
    )
    
    nodes["azure"] = kb.create_node(
        title="Microsoft Azure",
        content="Microsoftが提供するクラウドプラットフォーム。Windows環境との親和性が高く、企業向けサービスが充実。AI・機械学習サービスも豊富。",
        tags=["クラウド", "Azure", "Microsoft", "エンタープライズ", "AI"]
    )
    
    nodes["gcp"] = kb.create_node(
        title="Google Cloud Platform (GCP)",
        content="Googleが提供するクラウドサービス。機械学習、ビッグデータ処理に強み。Kubernetesの発祥でもあり、コンテナ技術が充実。",
        tags=["クラウド", "Google", "機械学習", "ビッグデータ", "Kubernetes"]
    )
    
    # コンテナ技術
    nodes["kubernetes"] = kb.create_node(
        title="Kubernetes",
        content="コンテナオーケストレーションプラットフォーム。コンテナ化されたアプリケーションの自動デプロイ、スケーリング、管理を行う。",
        tags=["コンテナ", "オーケストレーション", "Kubernetes", "自動化", "スケーリング"]
    )
    
    nodes["helm"] = kb.create_node(
        title="Helm",
        content="Kubernetesのパッケージマネージャー。複雑なKubernetesアプリケーションの管理を簡素化。テンプレート機能で設定の再利用が可能。",
        tags=["Kubernetes", "パッケージ管理", "テンプレート", "デプロイ", "設定管理"]
    )
    
    # CI/CD
    nodes["jenkins"] = kb.create_node(
        title="Jenkins",
        content="オープンソースの継続的インテグレーション・デリバリー（CI/CD）ツール。ビルド、テスト、デプロイの自動化を支援。豊富なプラグインエコシステム。",
        tags=["CI/CD", "自動化", "ビルド", "デプロイ", "オープンソース"]
    )
    
    nodes["github_actions"] = kb.create_node(
        title="GitHub Actions",
        content="GitHubが提供するCI/CDプラットフォーム。GitHubリポジトリと密結合し、ワークフローの自動化が可能。豊富なマーケットプレイスアクション。",
        tags=["CI/CD", "GitHub", "ワークフロー", "自動化", "統合"]
    )
    
    nodes["gitlab_ci"] = kb.create_node(
        title="GitLab CI/CD",
        content="GitLabに統合されたCI/CDシステム。Gitワークフローとシームレスに連携。パイプライン、ランナー、環境管理機能を提供。",
        tags=["CI/CD", "GitLab", "パイプライン", "DevOps", "統合"]
    )
    
    # インフラストラクチャー
    nodes["terraform"] = kb.create_node(
        title="Terraform",
        content="Infrastructure as Code (IaC) ツール。宣言的な設定ファイルでクラウドリソースを管理。多くのクラウドプロバイダーに対応。",
        tags=["IaC", "インフラ", "自動化", "HashiCorp", "宣言的"]
    )
    
    nodes["ansible"] = kb.create_node(
        title="Ansible",
        content="構成管理・自動化ツール。エージェントレスでサーバーの設定管理を行う。YAML形式のプレイブックで設定を記述。",
        tags=["構成管理", "自動化", "エージェントレス", "YAML", "Red Hat"]
    )
    
    # 監視・ログ
    nodes["prometheus"] = kb.create_node(
        title="Prometheus",
        content="オープンソースの監視・アラートシステム。メトリクス収集とクエリ機能を提供。Kubernetesとの親和性が高い。",
        tags=["監視", "メトリクス", "アラート", "時系列DB", "オープンソース"]
    )
    
    nodes["grafana"] = kb.create_node(
        title="Grafana",
        content="データ可視化・ダッシュボードツール。様々なデータソースからメトリクスを収集し、美しいグラフとして表示。",
        tags=["可視化", "ダッシュボード", "メトリクス", "グラフ", "監視"]
    )
    
    return nodes


def create_cloud_infrastructure_relationships(kb: KnowledgeBase, all_nodes: Dict[str, str]):
    """クラウド・インフラ技術間の関係性を作成"""
    
    # クラウドプロバイダー同士（競合関係）
    if "aws" in all_nodes and "azure" in all_nodes:
        kb.add_bidirectional_link(all_nodes["aws"], all_nodes["azure"])
    
    if "aws" in all_nodes and "gcp" in all_nodes:
        kb.add_bidirectional_link(all_nodes["aws"], all_nodes["gcp"])
    
    if "azure" in all_nodes and "gcp" in all_nodes:
        kb.add_bidirectional_link(all_nodes["azure"], all_nodes["gcp"])
    
    # Dockerとコンテナ技術
    if "docker" in all_nodes and "kubernetes" in all_nodes:
        kb.add_bidirectional_link(all_nodes["docker"], all_nodes["kubernetes"])
    
    if "kubernetes" in all_nodes and "helm" in all_nodes:
        kb.add_bidirectional_link(all_nodes["kubernetes"], all_nodes["helm"])
    
    # CI/CD間の関係
    if "jenkins" in all_nodes and "github_actions" in all_nodes:
        kb.add_bidirectional_link(all_nodes["jenkins"], all_nodes["github_actions"])
    
    if "github_actions" in all_nodes and "gitlab_ci" in all_nodes:
        kb.add_bidirectional_link(all_nodes["github_actions"], all_nodes["gitlab_ci"])
    
    # GitHub ActionsとGitHub
    if "github_actions" in all_nodes and "github" in all_nodes:
        kb.add_bidirectional_link(all_nodes["github_actions"], all_nodes["github"])
    
    # インフラ自動化ツール
    if "terraform" in all_nodes and "ansible" in all_nodes:
        kb.add_bidirectional_link(all_nodes["terraform"], all_nodes["ansible"])
    
    # 監視ツール
    if "prometheus" in all_nodes and "grafana" in all_nodes:
        kb.add_bidirectional_link(all_nodes["prometheus"], all_nodes["grafana"])
    
    # クラウドプロバイダーとサービス
    for cloud in ["aws", "azure", "gcp"]:
        if cloud in all_nodes:
            for service in ["kubernetes", "terraform", "prometheus"]:
                if service in all_nodes:
                    kb.add_bidirectional_link(all_nodes[cloud], all_nodes[service])
    
    # プログラミング言語との関係
    if "python" in all_nodes:
        for tool in ["terraform", "ansible", "kubernetes"]:
            if tool in all_nodes:
                kb.add_bidirectional_link(all_nodes["python"], all_nodes[tool])
    
    if "go" in all_nodes:
        for tool in ["kubernetes", "terraform", "prometheus"]:
            if tool in all_nodes:
                kb.add_bidirectional_link(all_nodes["go"], all_nodes[tool])
    
    # JavaScriptとの関係
    if "javascript" in all_nodes:
        for tool in ["github_actions", "grafana"]:
            if tool in all_nodes:
                kb.add_bidirectional_link(all_nodes["javascript"], all_nodes[tool])