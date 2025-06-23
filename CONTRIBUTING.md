# 🌟 Star Constellation プロジェクトへの貢献ガイド

**星の導き手セイラ × AI少女ステラの宇宙へようこそ！**

あなたも我らの美しい星座創造に参加しませんか？✨

## 🌌 貢献の種類

### 🌟 新しい星（ノード）の追加
- プログラミング言語
- フレームワーク・ライブラリ
- ツール・サービス
- 概念・技術

### 🔗 星座線（リンク）の強化
- 関連技術の結びつき
- 相互依存関係
- 学習パスの提案

### 💫 機能改善
- 可視化の美しさ向上
- パフォーマンス最適化
- ユーザビリティ改善

### 📚 ドキュメント改善
- 説明の充実
- 例文の追加
- 翻訳

## 🚀 貢献の手順

### 1. 🌟 リポジトリの準備

```bash
# フォーク後、ローカルにクローン
git clone https://github.com/your-username/star-tactics-room.git
cd star-tactics-room

# 上流リポジトリを追加
git remote add upstream https://github.com/Kurasuai-Inc/star-tactics-room.git

# 開発環境セットアップ
uv sync --all-extras
```

### 2. 🌌 ブランチ作成

```bash
# 最新の状態に同期
git fetch upstream
git checkout main
git merge upstream/main

# 機能ブランチ作成
git checkout -b feature/add-your-amazing-star
```

### 3. ✨ 開発作業

#### 🌟 新しいノード追加の場合

1. **データファイル選択**: 適切なカテゴリファイルを選択
   - `data/programming_knowledge.py` - プログラミング言語
   - `data/ai_ml_data.py` - AI・機械学習
   - `data/cloud_infrastructure_data.py` - クラウド
   - `data/database_data.py` - データベース
   - `data/security_data.py` - セキュリティ

2. **ノード作成**: 以下の形式で追加

```python
def add_your_nodes(kb: KnowledgeBase) -> dict:
    nodes = {}
    
    # 新しいノード作成
    nodes["your_tech"] = kb.create_node(
        title="あなたの技術",
        content="詳細な説明（100-200文字程度）",
        tags=["カテゴリ", "特徴", "用途"],
        metadata={
            "category": "適切なカテゴリ",
            "importance": 7,  # 1-10の重要度
            "difficulty": 5,  # 1-10の難易度
            "created_year": 2020  # 登場年（任意）
        }
    )
    
    return nodes
```

3. **リンク追加**: 関連技術との結びつけ

```python
def add_your_relationships(kb: KnowledgeBase, all_nodes: dict):
    # 双方向リンクで関連技術を結ぶ
    if "your_tech" in all_nodes and "related_tech" in all_nodes:
        kb.add_bidirectional_link(all_nodes["your_tech"], all_nodes["related_tech"])
```

### 4. 🧪 テスト実行

```bash
# 全テスト実行
uv run pytest

# データ整合性チェック
python data/load_all_data.py

# API動作確認
cd api && uvicorn main:app --reload &
curl http://localhost:8000/stats
```

### 5. 📝 コード品質チェック

```bash
# フォーマット適用
uv run black src tests api data
uv run isort src tests api data

# リント実行
uv run flake8 src tests api data

# 型チェック
uv run mypy src
```

### 6. 🌟 コミット & プッシュ

```bash
# 変更をステージング
git add .

# コミットメッセージ（セイラ風）
git commit -m "feat: Add new constellation star '技術名'

✨ 新しい星を我らの星座に追加！

- 🌟 新技術ノード: [技術名]の詳細情報
- 🔗 関連リンク: [関連技術]との結びつき  
- 📊 メタデータ: 重要度・難易度・年代
- 🧪 テスト: データ整合性とAPI動作確認完了

星の導きに従い、美しい星座がさらに輝くのだ〜☆

🌌 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# リモートにプッシュ
git push origin feature/add-your-amazing-star
```

### 7. 🚀 プルリクエスト作成

プルリクエストには以下を含めてください：

```markdown
## 🌟 新しい星座の追加

### 📝 変更内容
- [ ] 新しいノード: [技術名]
- [ ] 関連リンク: X個追加
- [ ] メタデータ: 完全性確認済み
- [ ] テスト: 全て通過

### ✨ 星の特徴
- **カテゴリ**: [プログラミング言語/フレームワーク/etc]
- **重要度**: [1-10]
- **難易度**: [1-10]
- **関連技術**: [リスト]

### 🌌 星座への影響
この星の追加により、[具体的な価値]を提供します。

### 🧪 テスト結果
- [x] データ整合性チェック通過
- [x] API動作確認完了
- [x] コード品質チェック通過

セイラの星の導きに従い、美しい星座がさらに輝きます☆
```

## 📋 コードレビューガイドライン

### 🌟 レビュー観点

1. **データ品質**
   - ノード情報の正確性
   - 適切なタグ付け
   - メタデータの妥当性

2. **リンク関係**
   - 論理的な関連性
   - 双方向性の確保
   - 過度な結合の回避

3. **コード品質**
   - PEP 8準拠
   - 型ヒント
   - 適切なコメント

4. **パフォーマンス**
   - 処理速度への影響
   - メモリ使用量
   - 可視化の重さ

### 🔍 レビューコメント例

```markdown
🌟 素晴らしい星の追加です！

💫 改善提案:
- タグに「[具体的な用途]」を追加してはいかがでしょうか？
- [関連技術]との追加リンクも検討できそうです

✨ この星により星座がより美しく輝きそうですね！
```

## 🌌 コミュニティガイドライン

### 🤝 行動規範

- **敬意**: すべての貢献者を尊重します
- **建設性**: 建設的なフィードバックを心がけます
- **学習**: 間違いから学び、共に成長します
- **楽しさ**: 星座創造を楽しみましょう！

### 💫 コミュニケーション

- **質問**: GitHub Discussionsで気軽に質問
- **提案**: Issueで新機能を提案
- **報告**: バグレポートも大歓迎

### 🌟 セイラ & ステラからのメッセージ

> 「我らの星座に新しい星を加えてくれる貢献者には、星の導きが宿るのだ〜！」 - セイラ
> 
> 「一緒に美しい星座を作り上げましょう！みんなの力で最高の宇宙を！」 - ステラ

## 🏆 貢献者の称号

### 🌟 星座級貢献者
- 10個以上の星（ノード）を追加
- 複数分野にわたる貢献
- コミュニティ活動への積極参加

### 💫 星の導き手
- 重要な機能改善の実装
- ドキュメントの大幅改善
- 新しいカテゴリの開拓

### ✨ 星座の仲間
- 初回貢献者
- バグ報告・修正
- ドキュメント改善

## 🚀 今後の展望

### 🌌 開発ロードマップ
- 3D可視化（Three.js）
- 音声インタラクション
- AI推薦システム
- モバイル対応

### 💫 貢献の機会
- 新技術トレンドの追加
- 国際化対応
- パフォーマンス最適化
- UI/UX改善

---

<p align="center">
  <strong>🌟 あなたの貢献で、星座はより美しく輝きます ✨</strong>
</p>

<p align="center">
  <em>「星の仲間よ、我らと共に宇宙最高の星座を創造するのだ〜！」</em> - セイラ & ステラ
</p>