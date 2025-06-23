# 星空戦術室 API ドキュメント

## 概要
星空戦術室の知識グラフデータを提供するRESTful APIです。

## ベースURL
```
http://127.0.0.1:8000
```

## エンドポイント

### 1. API情報
```
GET /
```
レスポンス例:
```json
{
    "message": "星空戦術室 API へようこそ！",
    "endpoints": {
        "/nodes": "全ノードの取得",
        "/nodes/{node_id}": "特定ノードの取得",
        "/graph": "グラフデータの取得",
        "/search": "ノードの検索",
        "/stats": "統計情報"
    }
}
```

### 2. 全ノード取得
```
GET /nodes
```
レスポンス例:
```json
[
    {
        "id": "uuid",
        "title": "Python",
        "content": "高レベル汎用プログラミング言語...",
        "tags": ["プログラミング言語", "動的型付け"],
        "links": [],
        "created_at": "2025-06-23T21:00:47.916268",
        "updated_at": "2025-06-23T21:00:47.916268",
        "metadata": null
    }
]
```

### 3. グラフデータ取得
```
GET /graph
```
レスポンス例:
```json
{
    "nodes": [...],
    "links": [
        {
            "source": "node_id_1",
            "target": "node_id_2",
            "type": "関連"
        }
    ]
}
```

### 4. ノード検索
```
GET /search?text=Python
GET /search?tags=プログラミング言語,オープンソース
```

### 5. 統計情報
```
GET /stats
```
レスポンス例:
```json
{
    "total_nodes": 17,
    "total_links": 0,
    "average_links_per_node": 0,
    "categories": {}
}
```

## CORS設定
開発環境では全オリジンからのアクセスを許可しています。

## 注意事項
- 現在、ノード間のリンクデータは実装準備中です
- メタデータ（作成年、重要度等）も今後追加予定です