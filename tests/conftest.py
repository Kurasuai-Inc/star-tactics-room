"""pytest共通設定とフィクスチャ"""

import pytest


@pytest.fixture
def sample_data():
    """テスト用のサンプルデータを提供するフィクスチャ"""
    return {
        "name": "テスト戦術",
        "description": "これはテスト用の戦術です",
        "tags": ["テスト", "サンプル"],
    }
