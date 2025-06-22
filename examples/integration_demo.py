#!/usr/bin/env python3
"""統合デモ: データ永続化とリンク管理を組み合わせた使用例"""

from pathlib import Path
from star_tactics.models.knowledge_node import KnowledgeBase
from star_tactics.storage import JSONStorage


def main():
    """メイン実行関数"""
    # JSONストレージを使用してKnowledgeBaseを初期化
    storage_path = Path("knowledge_base.json")
    storage = JSONStorage(storage_path)
    kb = KnowledgeBase(storage=storage)
    
    print("=== 星空戦術室 統合デモ ===\n")
    
    # 既存のデータがあるか確認
    existing_nodes = kb.get_all_nodes()
    if existing_nodes:
        print(f"既存のノード数: {len(existing_nodes)}")
        for node in existing_nodes:
            print(f"  - {node.title} (ID: {node.id})")
        print()
    else:
        print("新規のKnowledgeBaseを作成します\n")
        
        # サンプルノードを作成
        print("1. ノードを作成中...")
        
        # 戦術関連のノード
        tactics_id = kb.create_node(
            title="基本戦術パターン",
            content="星空戦術室における基本的な戦術パターンの概要",
            tags=["戦術", "基本", "パターン"]
        )
        print(f"   ✓ 基本戦術パターン (ID: {tactics_id})")
        
        # 装備関連のノード
        equipment_id = kb.create_node(
            title="推奨装備セット",
            content="各戦術パターンに対応する推奨装備の組み合わせ",
            tags=["装備", "推奨", "セット"]
        )
        print(f"   ✓ 推奨装備セット (ID: {equipment_id})")
        
        # スキル関連のノード
        skills_id = kb.create_node(
            title="必須スキル一覧",
            content="効果的な戦術実行に必要なスキルのリスト",
            tags=["スキル", "必須", "一覧"]
        )
        print(f"   ✓ 必須スキル一覧 (ID: {skills_id})")
        
        # 実戦例のノード
        example_id = kb.create_node(
            title="実戦サンプル: 防衛戦",
            content="防衛戦における戦術パターンの実例",
            tags=["実戦", "サンプル", "防衛"]
        )
        print(f"   ✓ 実戦サンプル (ID: {example_id})")
        
        print("\n2. 双方向リンクを設定中...")
        
        # 戦術と装備を双方向リンク
        kb.add_bidirectional_link(tactics_id, equipment_id)
        print("   ✓ 基本戦術パターン ↔ 推奨装備セット")
        
        # 戦術とスキルを双方向リンク
        kb.add_bidirectional_link(tactics_id, skills_id)
        print("   ✓ 基本戦術パターン ↔ 必須スキル一覧")
        
        # 戦術と実戦例を双方向リンク
        kb.add_bidirectional_link(tactics_id, example_id)
        print("   ✓ 基本戦術パターン ↔ 実戦サンプル")
        
        # 装備とスキルを双方向リンク
        kb.add_bidirectional_link(equipment_id, skills_id)
        print("   ✓ 推奨装備セット ↔ 必須スキル一覧")
        
        print(f"\n✓ データは自動的に {storage_path} に保存されました")
    
    # 検索機能のデモ
    print("\n3. 検索機能のデモ")
    
    # タグで検索
    print("   - '戦術'タグで検索:")
    tactics_nodes = kb.search_by_tags(["戦術"])
    for node in tactics_nodes:
        print(f"     ✓ {node.title}")
    
    # テキスト検索
    print("   - 'スキル'を含むノードを検索:")
    skill_nodes = kb.search_by_text("スキル")
    for node in skill_nodes:
        print(f"     ✓ {node.title}")
    
    # リンク管理機能のデモ
    print("\n4. リンク管理機能のデモ")
    
    # 基本戦術パターンのリンクを確認
    tactics_node = kb.get_node(tactics_id) if 'tactics_id' in locals() else existing_nodes[0]
    if tactics_node:
        print(f"   - '{tactics_node.title}'のリンク数: {len(tactics_node.links)}")
        
        # リンクの検証
        if kb.validate_links(tactics_node.id):
            print("     ✓ 全てのリンクが有効です")
        else:
            print("     ✗ 無効なリンクが存在します")
            broken_links = kb.get_broken_links(tactics_node.id)
            if broken_links:
                print(f"       壊れたリンク: {broken_links}")
                print("       自動修復を実行...")
                fixed_count = kb.fix_broken_links(tactics_node.id)
                print(f"       ✓ {fixed_count}個のリンクを修復しました")
    
    # 全体のリンク状態確認
    all_broken = kb.get_all_broken_links()
    if all_broken:
        print(f"\n   ⚠ 全体で{len(all_broken)}個のノードに壊れたリンクがあります")
    else:
        print("\n   ✓ 全てのノードのリンクが正常です")
    
    print("\n=== デモ完了 ===")
    print(f"KnowledgeBaseは {storage_path} に保存されています")
    print("再実行すると、保存されたデータが自動的に読み込まれます")


if __name__ == "__main__":
    main()