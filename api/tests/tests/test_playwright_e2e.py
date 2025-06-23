"""Playwright E2Eテスト - 星座ビューアー統合テスト"""

import asyncio
import pytest
import subprocess
import time
import signal
import requests
from pathlib import Path
from playwright.async_api import async_playwright, expect


class TestStarConstellationE2E:
    """星座ビューアーのEnd-to-Endテスト"""
    
    @classmethod
    def setup_class(cls):
        """テストクラス開始時にサーバーを起動"""
        cls.api_url = "http://127.0.0.1:8001"
        cls.frontend_url = "http://localhost:5173"
        cls.api_process = None
        cls.frontend_process = None
        
        # APIサーバー起動
        try:
            cls.api_process = subprocess.Popen([
                "uv", "run", "uvicorn", "api.main:app", 
                "--host", "127.0.0.1", "--port", "8001"
            ], cwd=Path(__file__).parent.parent)
            
            # APIサーバー起動待機
            for _ in range(30):
                try:
                    response = requests.get(f"{cls.api_url}/", timeout=1)
                    if response.status_code == 200:
                        print("✅ APIサーバー起動完了")
                        break
                except requests.exceptions.RequestException:
                    pass
                time.sleep(1)
            else:
                raise Exception("APIサーバーの起動に失敗しました")
        
        except Exception as e:
            print(f"サーバー起動エラー: {e}")
            if cls.api_process:
                cls.api_process.terminate()
            raise
    
    @classmethod
    def teardown_class(cls):
        """テストクラス終了時にサーバーを停止"""
        if cls.api_process:
            cls.api_process.terminate()
            cls.api_process.wait()
        
        if cls.frontend_process:
            cls.frontend_process.terminate()
            cls.frontend_process.wait()
    
    async def test_api_health_check(self):
        """APIヘルスチェック"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            # APIエンドポイントに直接アクセス
            await page.goto(f"{self.api_url}/stats")
            
            # JSONレスポンスを確認
            content = await page.content()
            assert "total_nodes" in content
            assert "101" in content  # セイラの101ノード
            
            await browser.close()
    
    async def test_api_optimized_endpoint(self):
        """最適化APIエンドポイントテスト"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            # 最適化エンドポイントアクセス
            await page.goto(f"{self.api_url}/graph/optimized")
            
            # JSONレスポンスを確認
            content = await page.content()
            assert "optimization_info" in content
            assert "selected_nodes" in content
            
            await browser.close()
    
    async def test_api_performance(self):
        """APIパフォーマンステスト"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            # レスポンス時間測定
            start_time = time.time()
            response = await page.goto(f"{self.api_url}/graph/optimized")
            end_time = time.time()
            
            # 3秒以内のレスポンス時間を確認
            response_time = end_time - start_time
            assert response_time < 3.0, f"API response too slow: {response_time}s"
            assert response.status == 200
            
            await browser.close()
    
    async def test_api_data_consistency(self):
        """APIデータ整合性テスト"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            
            # 統計情報を取得
            await page.goto(f"{self.api_url}/stats")
            stats_content = await page.content()
            
            # グラフデータを取得
            await page.goto(f"{self.api_url}/graph")
            graph_content = await page.content()
            
            # 最適化データを取得
            await page.goto(f"{self.api_url}/graph/optimized")
            optimized_content = await page.content()
            
            # データ整合性確認
            assert "101" in stats_content  # ノード数
            assert "508" in stats_content  # リンク数
            assert "nodes" in graph_content
            assert "links" in graph_content
            assert "optimization_info" in optimized_content
            
            await browser.close()
    
    async def test_concurrent_api_access(self):
        """同時APIアクセステスト"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            
            # 複数のコンテキストで同時アクセス
            tasks = []
            for i in range(5):
                context = await browser.new_context()
                page = await context.new_page()
                
                async def fetch_data():
                    response = await page.goto(f"{self.api_url}/stats")
                    assert response.status == 200
                    await context.close()
                
                tasks.append(fetch_data())
            
            # 並行実行
            await asyncio.gather(*tasks)
            await browser.close()


def run_manual_tests():
    """手動実行用のテストランナー"""
    async def main():
        test_instance = TestStarConstellationE2E()
        
        print("🎭 Playwright E2Eテスト開始...")
        
        try:
            TestStarConstellationE2E.setup_class()
            
            await test_instance.test_api_health_check()
            print("✅ APIヘルスチェック完了")
            
            await test_instance.test_api_optimized_endpoint()
            print("✅ 最適化エンドポイントテスト完了")
            
            await test_instance.test_api_performance()
            print("✅ パフォーマンステスト完了")
            
            await test_instance.test_api_data_consistency()
            print("✅ データ整合性テスト完了")
            
            await test_instance.test_concurrent_api_access()
            print("✅ 同時アクセステスト完了")
            
            print("🌌 Playwright E2Eテスト - 全て成功！")
            
        except Exception as e:
            print(f"❌ E2Eテスト失敗: {e}")
            
        finally:
            TestStarConstellationE2E.teardown_class()
            print("🔚 サーバー停止完了")
    
    asyncio.run(main())


if __name__ == "__main__":
    run_manual_tests()