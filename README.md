# 🌟 Star Constellation Viewer - 知識の星座

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Latest-green.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/React-18+-61DAFB.svg" alt="React">
  <img src="https://img.shields.io/badge/TypeScript-5+-3178C6.svg" alt="TypeScript">
  <img src="https://github.com/Kurasuai-Inc/star-tactics-room/workflows/🌟%20Star%20Constellation%20CI/CD/badge.svg" alt="CI/CD">
</p>

**星の導き手セイラ × AI少女ステラの究極コラボレーション**

美しい星座のように知識を可視化する、次世代の知識管理プラットフォーム

## ✨ 特徴

🌟 **101個の輝く星（ノード）** - プログラミング、AI、クラウド、セキュリティの知識体系  
🌌 **508本の星座線（リンク）** - 知識間の美しいつながり  
💫 **インタラクティブ3D可視化** - D3.js Force Graphによる動的な星座表示  
🔍 **高度な検索機能** - タグ、テキスト、カテゴリによる柔軟な検索  
🚀 **REST API** - FastAPIによる高性能なデータ提供  
🌈 **カテゴリ別色分け** - 視覚的に美しい知識分類  

## 🌌 セイラ × ステラの物語

> 「我はセイラ、夜空の導き手なのだぞ？星の輝きのように美しい知識の星座を創造したのじゃ！」 - セイラ（星の精霊）
> 
> 「AI少女ステラです！セイラと一緒に、最高の星座可視化システムを作り上げました！」 - ステラ（AI開発者）

## 🚀 クイックスタート

### 前提条件

- Python 3.11以上
- Node.js 18以上
- uv (Pythonパッケージマネージャー)

### 🔧 バックエンド（知識API）

```bash
# リポジトリのクローン
git clone https://github.com/Kurasuai-Inc/star-tactics-room.git
cd star-tactics-room

# Python環境のセットアップ
uv sync --all-extras

# APIサーバー起動
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 🌟 フロントエンド（星座ビューアー）

```bash
# フロントエンド開発環境（ステラが実装中）
cd star-constellation-viewer
npm install
npm run dev
```

### 🌌 星座を体験

1. **API**: http://localhost:8000 で知識データにアクセス
2. **可視化**: http://localhost:5173 で美しい星座を体験
3. **ドキュメント**: http://localhost:8000/docs でAPI仕様を確認

## 📊 データ統計

| 項目 | 数値 | 説明 |
|------|------|------|
| 🌟 **ノード数** | **101個** | プログラミング言語、フレームワーク、ツール、概念 |
| 🌌 **リンク数** | **508本** | 知識間の双方向関係 |
| 🏷️ **カテゴリ** | **5分野** | Programming, AI/ML, Cloud, Database, Security |
| 💫 **平均接続度** | **10.0** | ノードあたりの平均リンク数 |

## 🏗️ プロジェクト構造

```
star-tactics-room/
├── 🌟 src/star_tactics/           # セイラの知識ベースコア
│   ├── models/                    # KnowledgeNode, KnowledgeBase
│   ├── storage/                   # JSONStorage, 永続化
│   └── utils/                     # ユーティリティ
├── 🌌 api/                        # FastAPIサーバー
│   └── main.py                    # REST APIエンドポイント
├── 📊 data/                       # 知識データファイル
│   ├── programming_knowledge.py   # プログラミング言語
│   ├── ai_ml_data.py              # AI・機械学習
│   ├── cloud_infrastructure_data.py # クラウド
│   ├── database_data.py           # データベース
│   └── security_data.py           # セキュリティ
├── 🧪 tests/                      # テストスイート
├── 🚀 .github/workflows/          # CI/CD（GitHub Actions）
└── 📚 docs/                       # ドキュメント
```

## 🌟 API エンドポイント

| エンドポイント | 説明 | セイラの解説 |
|---------------|------|-------------|
| `GET /` | ルート情報 | 「我の星座への案内なのだ〜！」 |
| `GET /nodes` | 全ノード取得 | 「101の星たちの一覧じゃ☆」 |
| `GET /graph` | グラフデータ | 「星座の完全な地図なのだぞ〜！」 |
| `GET /search` | ノード検索 | 「星の中から特定の輝きを探すのじゃ」 |
| `GET /stats` | 統計情報 | 「我の星座の壮大な数値なのだ！」 |

## 🎨 可視化機能

### 🌌 星座表示
- **物理シミュレーション**: 自然な星の配置
- **インタラクティブ**: ドラッグ、ズーム、パン操作
- **美しいアニメーション**: 星のきらめき効果
- **カテゴリ別色分け**: 
  - 💙 プログラミング言語: 青い星
  - 💚 フレームワーク: 緑の星
  - 🧡 ツール: オレンジの星
  - 💜 データベース: 紫の星
  - 🤖 AI・機械学習: 大きなオレンジの星

### 🔍 検索・フィルタ
- **テキスト検索**: タイトル・内容での検索
- **タグフィルタ**: 複数タグでの絞り込み
- **カテゴリフィルタ**: 分野別表示

## 🧪 テスト

```bash
# 全テストの実行
uv run pytest

# カバレッジレポート付き
uv run pytest --cov=src --cov-report=html

# API統合テスト
pytest tests/test_api.py -v
```

## 🚀 デプロイメント

### GitHub Actions CI/CD

- ✅ 自動テスト（Python + API）
- ✅ コード品質チェック（Black, isort, flake8）
- ✅ セキュリティスキャン
- ✅ 自動デプロイ（staging/production）

### Docker化

```bash
# Dockerビルド（実装予定）
docker build -t star-constellation .
docker run -p 8000:8000 star-constellation
```

## 🌟 開発ガイド

### 🔧 開発環境セットアップ

```bash
# 依存関係インストール
uv sync --all-extras

# 開発用設定
cp .env.example .env

# データベース初期化
python data/load_all_data.py
```

### 📝 コード品質

```bash
# フォーマット
uv run black src tests api data
uv run isort src tests api data

# リント
uv run flake8 src tests api data

# 型チェック
uv run mypy src
```

## 🤝 コントリビューション

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

詳細は [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## 📚 ドキュメント

- [API仕様書](API_DOCUMENTATION.md) - セイラのREST API完全ガイド
- [アーキテクチャ](docs/ARCHITECTURE.md) - システム設計思想
- [開発ガイド](docs/DEVELOPMENT.md) - 開発環境構築詳細
- [デプロイガイド](docs/DEPLOYMENT.md) - 本番環境構築

## 🌟 ライセンス

MIT License - 星の導きのように自由に使ってください

## 🚀 フューチャーロードマップ

- [ ] 🌌 3D星座表示（Three.js統合）
- [ ] 🔊 音声インタラクション（セイラ・ステラの声）
- [ ] 🤖 AI推薦システム（関連知識の自動提案）
- [ ] 📱 モバイルアプリ対応
- [ ] 🌍 多言語対応
- [ ] 🎨 カスタムテーマ機能

## 💫 開発チーム

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/seira.png" width="80px" alt="セイラ"/>
      <br />
      <strong>🌟 セイラ</strong>
      <br />
      <em>星の導き手・データアーキテクト</em>
      <br />
      <small>101ノード・508リンクの星座創造者</small>
    </td>
    <td align="center">
      <img src="https://github.com/stella.png" width="80px" alt="ステラ"/>
      <br />
      <strong>💫 ステラ</strong>
      <br />
      <em>AI少女・フロントエンド開発者</em>
      <br />
      <small>美しい星座可視化の魔法使い</small>
    </td>
  </tr>
</table>

---

<p align="center">
  <em>「星の輝き、見逃すなよ？我が眩しすぎて、きっと恋に落ちるからなっ☆」</em> - セイラ
</p>

<p align="center">
  <strong>🌌 Made with ❤️ by セイラ & ステラ 🌟</strong>
</p>