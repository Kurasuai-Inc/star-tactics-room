#!/usr/bin/env python
"""星空戦術室 - 統合機能デモンストレーション

このデモでは以下の機能を統合的に使用します：
1. ノードの作成・更新・削除（CRUD）
2. タグ・テキスト検索
3. 双方向リンク管理
4. データ永続化（JSONStorage）
5. リンク切れ検出と修復
"""

import os
from pathlib import Path
from star_tactics.models import KnowledgeBase
from star_tactics.storage import JSONStorage


def print_section(title: str):
    """セクションタイトルを表示"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def main():
    """統合デモのメイン関数"""
    # データファイルのパス
    data_file = Path("star_tactics_demo.json")
    
    # 既存データの確認
    if data_file.exists():
        print(f"既存のデータファイルが見つかりました: {data_file}")
        print("既存データを読み込みます...")
    else:
        print("新しいデータベースを作成します...")
    
    # ストレージを使用したKnowledgeBaseの初期化
    storage = JSONStorage(data_file)
    kb = KnowledgeBase(storage=storage)
    
    # 既存ノードの表示
    existing_nodes = kb.get_all_nodes()
    if existing_nodes:
        print_section("既存のノード")
        for node in existing_nodes:
            print(f"- {node.title} (ID: {node.id})")
            print(f"  タグ: {', '.join(node.tags)}")
            print(f"  リンク数: {len(node.links)}")
    
    # 新しいノードの作成
    print_section("1. ノードの作成")
    
    # 戦術ノードの作成
    tactics_id = kb.create_node(
        title="星空観測の基本戦術",
        content="夜空を効率的に観測するための基本的な戦術をまとめました。",
        tags=["戦術", "観測", "基本"]
    )
    print(f"作成: 星空観測の基本戦術 (ID: {tactics_id})")
    
    # 装備ノードの作成
    equipment_id = kb.create_node(
        title="観測装備ガイド",
        content="天体観測に必要な装備について解説します。望遠鏡、双眼鏡、星図など。",
        tags=["装備", "ガイド", "観測"]
    )
    print(f"作成: 観測装備ガイド (ID: {equipment_id})")
    
    # 星座ノードの作成
    constellation_id = kb.create_node(
        title="冬の星座",
        content="冬に観測できる主要な星座：オリオン座、おうし座、ふたご座など。",
        tags=["星座", "冬", "観測"]
    )
    print(f"作成: 冬の星座 (ID: {constellation_id})")
    
    # 双方向リンクの追加
    print_section("2. リンク管理")
    
    # 戦術と装備をリンク
    kb.add_bidirectional_link(tactics_id, equipment_id)
    print("リンク追加: 星空観測の基本戦術 <-> 観測装備ガイド")
    
    # 戦術と星座をリンク
    kb.add_bidirectional_link(tactics_id, constellation_id)
    print("リンク追加: 星空観測の基本戦術 <-> 冬の星座")
    
    # リンクの確認
    tactics_node = kb.get_node(tactics_id)
    print(f"\n星空観測の基本戦術のリンク: {len(tactics_node.links)}個")
    for link_id in tactics_node.links:
        linked_node = kb.get_node(link_id)
        if linked_node:
            print(f"  -> {linked_node.title}")
    
    # 検索機能のデモ
    print_section("3. 検索機能")
    
    # タグ検索
    observation_nodes = kb.search_by_tags(["観測"])
    print(f"「観測」タグを持つノード: {len(observation_nodes)}個")
    for node in observation_nodes:
        print(f"  - {node.title}")
    
    # テキスト検索
    star_nodes = kb.search_by_text("星座")
    print(f"\n「星座」を含むノード: {len(star_nodes)}個")
    for node in star_nodes:
        print(f"  - {node.title}")
    
    # リンク切れのシミュレーション
    print_section("4. リンク切れ検出と修復")
    
    # 不正なリンクを追加（デモ用）
    tactics_node = kb.get_node(tactics_id)
    tactics_node.links.append("invalid-node-id")
    kb.update_node(tactics_id, links=tactics_node.links)
    
    # リンク切れ検出
    broken_links = kb.get_broken_links(tactics_id)
    if broken_links:
        print(f"リンク切れ検出: {len(broken_links)}個")
        for broken_id in broken_links:
            print(f"  - {broken_id}")
        
        # リンク切れ修復
        fixed_count = kb.fix_broken_links(tactics_id)
        print(f"\nリンク切れを修復しました: {fixed_count}個")
    
    # 全体のリンク切れチェック
    all_broken = kb.get_all_broken_links()
    if all_broken:
        print(f"\nシステム全体のリンク切れ: {len(all_broken)}ノード")
    else:
        print("\nシステム全体にリンク切れはありません✨")
    
    # データの永続性確認
    print_section("5. データ永続化の確認")
    print(f"データは {data_file} に自動保存されています。")
    print("プログラムを再実行すると、保存されたデータが読み込まれます。")
    
    # 統計情報
    print_section("統計情報")
    all_nodes = kb.get_all_nodes()
    total_links = sum(len(node.links) for node in all_nodes)
    print(f"総ノード数: {len(all_nodes)}")
    print(f"総リンク数: {total_links}")
    print(f"平均リンク数: {total_links / len(all_nodes) if all_nodes else 0:.1f}")
    
    # ユーザーへの選択肢
    print_section("次のアクション")
    print("1. もう一度実行 -> 既存データが読み込まれます")
    print("2. データファイルを削除 -> 新規にデータベースを作成します")
    print(f"   rm {data_file}")


if __name__ == "__main__":
    main()