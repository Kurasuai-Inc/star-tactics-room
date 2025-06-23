#!/usr/bin/env python
"""セキュリティ技術の知識ノードを作成"""

from typing import Dict
from star_tactics.models import KnowledgeBase


def create_security_data(kb: KnowledgeBase) -> Dict[str, str]:
    """セキュリティ技術の知識ノードを作成"""
    nodes = {}
    
    # 認証・認可
    nodes["oauth2"] = kb.create_node(
        title="OAuth 2.0",
        content="認可フレームワークの標準プロトコル。サードパーティアプリケーションに対してリソースへの限定的なアクセスを許可。Web APIの認可によく使用される。",
        tags=["セキュリティ", "認証", "認可", "OAuth", "API"]
    )
    
    nodes["jwt"] = kb.create_node(
        title="JSON Web Token (JWT)",
        content="JSON形式でクレームを安全に送信するためのトークン標準。デジタル署名により改ざんを検出。ステートレスな認証に適している。",
        tags=["セキュリティ", "認証", "JWT", "トークン", "JSON"]
    )
    
    nodes["openid_connect"] = kb.create_node(
        title="OpenID Connect",
        content="OAuth 2.0の上に構築された認証プロトコル。ユーザーのアイデンティティ確認とシングルサインオン（SSO）を可能にする。",
        tags=["セキュリティ", "認証", "OpenID", "SSO", "OAuth"]
    )
    
    nodes["saml"] = kb.create_node(
        title="SAML",
        content="Security Assertion Markup Language。XML ベースの認証・認可データ交換標準。エンタープライズ環境でのSSO実装によく使用される。",
        tags=["セキュリティ", "認証", "SAML", "XML", "エンタープライズ"]
    )
    
    # 暗号化
    nodes["tls"] = kb.create_node(
        title="TLS/SSL",
        content="Transport Layer Security。インターネット通信を暗号化するプロトコル。HTTPS、メール、VPNなど様々な通信で使用される。",
        tags=["セキュリティ", "暗号化", "TLS", "SSL", "HTTPS"]
    )
    
    nodes["aes"] = kb.create_node(
        title="AES",
        content="Advanced Encryption Standard。対称鍵暗号化アルゴリズムの標準。高いセキュリティと性能を両立し、広く使用されている。",
        tags=["セキュリティ", "暗号化", "AES", "対称鍵", "アルゴリズム"]
    )
    
    nodes["rsa"] = kb.create_node(
        title="RSA",
        content="公開鍵暗号システムの代表的なアルゴリズム。デジタル署名と暗号化に使用。TLSやSSHなどで広く採用されている。",
        tags=["セキュリティ", "暗号化", "RSA", "公開鍵", "デジタル署名"]
    )
    
    # セキュリティツール
    nodes["hashicorp_vault"] = kb.create_node(
        title="HashiCorp Vault",
        content="秘密情報管理ツール。パスワード、APIキー、証明書などを安全に保存・管理。動的秘密情報生成や暗号化サービスも提供。",
        tags=["セキュリティ", "秘密管理", "HashiCorp", "暗号化", "API"]
    )
    
    nodes["letsencrypt"] = kb.create_node(
        title="Let's Encrypt",
        content="無料で自動化されたTLS証明書発行機関。WebサイトのHTTPS化を簡単に実現。ACMEプロトコルによる自動更新が可能。",
        tags=["セキュリティ", "証明書", "TLS", "無料", "自動化"]
    )
    
    nodes["owasp"] = kb.create_node(
        title="OWASP",
        content="Open Web Application Security Project。Webアプリケーションセキュリティの向上を目指す非営利団体。OWASP Top 10など有名なガイドラインを発行。",
        tags=["セキュリティ", "Web", "脆弱性", "ガイドライン", "教育"]
    )
    
    # 脆弱性・攻撃
    nodes["xss"] = kb.create_node(
        title="Cross-Site Scripting (XSS)",
        content="Webアプリケーションの脆弱性の一種。悪意のあるスクリプトをWebページに埋め込み、他のユーザーのブラウザで実行させる攻撃。",
        tags=["セキュリティ", "脆弱性", "XSS", "Web", "攻撃"]
    )
    
    nodes["sql_injection"] = kb.create_node(
        title="SQL Injection",
        content="データベースクエリに悪意のあるSQLコードを挿入する攻撃。不適切な入力検証により発生。データ漏洩や改ざんの原因となる。",
        tags=["セキュリティ", "脆弱性", "SQL", "データベース", "攻撃"]
    )
    
    nodes["csrf"] = kb.create_node(
        title="Cross-Site Request Forgery (CSRF)",
        content="認証されたユーザーに意図しない操作を実行させる攻撃。CSRFトークンや適切な認証チェックで防御可能。",
        tags=["セキュリティ", "脆弱性", "CSRF", "Web", "攻撃"]
    )
    
    return nodes


def create_security_relationships(kb: KnowledgeBase, all_nodes: Dict[str, str]):
    """セキュリティ技術間の関係性を作成"""
    
    # 認証・認可プロトコル間の関係
    if "oauth2" in all_nodes and "openid_connect" in all_nodes:
        kb.add_bidirectional_link(all_nodes["oauth2"], all_nodes["openid_connect"])
    
    if "oauth2" in all_nodes and "jwt" in all_nodes:
        kb.add_bidirectional_link(all_nodes["oauth2"], all_nodes["jwt"])
    
    if "openid_connect" in all_nodes and "saml" in all_nodes:
        kb.add_bidirectional_link(all_nodes["openid_connect"], all_nodes["saml"])
    
    # 暗号化技術間の関係
    if "tls" in all_nodes and "rsa" in all_nodes:
        kb.add_bidirectional_link(all_nodes["tls"], all_nodes["rsa"])
    
    if "tls" in all_nodes and "aes" in all_nodes:
        kb.add_bidirectional_link(all_nodes["tls"], all_nodes["aes"])
    
    if "letsencrypt" in all_nodes and "tls" in all_nodes:
        kb.add_bidirectional_link(all_nodes["letsencrypt"], all_nodes["tls"])
    
    # セキュリティツール間の関係
    if "hashicorp_vault" in all_nodes and "jwt" in all_nodes:
        kb.add_bidirectional_link(all_nodes["hashicorp_vault"], all_nodes["jwt"])
    
    if "owasp" in all_nodes and "xss" in all_nodes:
        kb.add_bidirectional_link(all_nodes["owasp"], all_nodes["xss"])
    
    if "owasp" in all_nodes and "sql_injection" in all_nodes:
        kb.add_bidirectional_link(all_nodes["owasp"], all_nodes["sql_injection"])
    
    if "owasp" in all_nodes and "csrf" in all_nodes:
        kb.add_bidirectional_link(all_nodes["owasp"], all_nodes["csrf"])
    
    # 脆弱性間の関係
    if "xss" in all_nodes and "csrf" in all_nodes:
        kb.add_bidirectional_link(all_nodes["xss"], all_nodes["csrf"])
    
    # フレームワークとセキュリティ
    if "fastapi" in all_nodes:
        for sec in ["oauth2", "jwt", "tls"]:
            if sec in all_nodes:
                kb.add_bidirectional_link(all_nodes["fastapi"], all_nodes[sec])
    
    if "django" in all_nodes:
        for sec in ["csrf", "xss", "oauth2"]:
            if sec in all_nodes:
                kb.add_bidirectional_link(all_nodes["django"], all_nodes[sec])
    
    if "express" in all_nodes:
        for sec in ["jwt", "oauth2", "xss", "csrf"]:
            if sec in all_nodes:
                kb.add_bidirectional_link(all_nodes["express"], all_nodes[sec])
    
    # データベースとセキュリティ
    for db in ["mysql", "postgresql", "mongodb"]:
        if db in all_nodes and "sql_injection" in all_nodes:
            kb.add_bidirectional_link(all_nodes[db], all_nodes["sql_injection"])
    
    # クラウドとセキュリティ
    for cloud in ["aws", "azure", "gcp"]:
        if cloud in all_nodes:
            for sec in ["oauth2", "tls", "hashicorp_vault"]:
                if sec in all_nodes:
                    kb.add_bidirectional_link(all_nodes[cloud], all_nodes[sec])