"""Tests for search functionality in KnowledgeBase."""

import pytest
from star_tactics.models.knowledge_node import KnowledgeBase


class TestKnowledgeBaseSearch:
    """Test search operations for KnowledgeBase."""

    @pytest.fixture
    def knowledge_base_with_data(self):
        """Provide a KnowledgeBase with sample data."""
        kb = KnowledgeBase()

        # Add test nodes
        kb.create_node(
            title="Python Programming",
            content="Python is a high-level programming language",
            tags=["python", "programming", "language"],
        )

        kb.create_node(
            title="星空観測ガイド",
            content="夜空の星を観測するための基本的なガイド",
            tags=["astronomy", "星空", "観測"],
        )

        kb.create_node(
            title="Machine Learning Basics",
            content="Introduction to machine learning concepts and algorithms",
            tags=["machine-learning", "ai", "python"],
        )

        kb.create_node(
            title="Web Development",
            content="Building web applications with modern frameworks",
            tags=["web", "programming", "javascript"],
        )

        return kb

    def test_search_by_single_tag(self, knowledge_base_with_data):
        """Test searching nodes by a single tag."""
        results = knowledge_base_with_data.search_by_tags(["python"])

        assert len(results) == 2
        titles = [node.title for node in results]
        assert "Python Programming" in titles
        assert "Machine Learning Basics" in titles

    def test_search_by_multiple_tags_and(self, knowledge_base_with_data):
        """Test AND search with multiple tags."""
        results = knowledge_base_with_data.search_by_tags(["python", "programming"])

        assert len(results) == 1
        assert results[0].title == "Python Programming"

    def test_search_by_title_partial_match(self, knowledge_base_with_data):
        """Test searching by partial title match."""
        results = knowledge_base_with_data.search_by_text("Python")

        assert len(results) == 1
        assert results[0].title == "Python Programming"

    def test_search_by_content_partial_match(self, knowledge_base_with_data):
        """Test searching by partial content match."""
        results = knowledge_base_with_data.search_by_text("machine learning")

        assert len(results) == 1
        assert results[0].title == "Machine Learning Basics"

    def test_search_japanese_text(self, knowledge_base_with_data):
        """Test searching with Japanese text."""
        results = knowledge_base_with_data.search_by_text("星空")

        assert len(results) == 1
        assert results[0].title == "星空観測ガイド"

    def test_search_by_japanese_tag(self, knowledge_base_with_data):
        """Test searching by Japanese tag."""
        results = knowledge_base_with_data.search_by_tags(["観測"])

        assert len(results) == 1
        assert results[0].title == "星空観測ガイド"

    def test_search_empty_results(self, knowledge_base_with_data):
        """Test search that returns no results."""
        results = knowledge_base_with_data.search_by_text("nonexistent")
        assert len(results) == 0

        results = knowledge_base_with_data.search_by_tags(["nonexistent-tag"])
        assert len(results) == 0

    def test_search_case_insensitive(self, knowledge_base_with_data):
        """Test case-insensitive search."""
        # Search by text - different cases
        results = knowledge_base_with_data.search_by_text("python")
        assert len(results) == 1

        results = knowledge_base_with_data.search_by_text("PYTHON")
        assert len(results) == 1

        results = knowledge_base_with_data.search_by_text("Python")
        assert len(results) == 1

        # Search by tag - different cases
        results = knowledge_base_with_data.search_by_tags(["PYTHON"])
        assert len(results) == 2

    def test_search_multiple_matches(self, knowledge_base_with_data):
        """Test search that returns multiple results."""
        # Search for "language" which appears in Python content
        results = knowledge_base_with_data.search_by_text("language")

        assert len(results) == 1
        assert results[0].title == "Python Programming"

        # Search for "application" which appears in Web Development content
        results = knowledge_base_with_data.search_by_text("application")

        assert len(results) == 1
        assert results[0].title == "Web Development"

    def test_search_all_nodes(self, knowledge_base_with_data):
        """Test getting all nodes when no search criteria provided."""
        results = knowledge_base_with_data.get_all_nodes()

        assert len(results) == 4

    def test_search_by_text_includes_title_and_content(self, knowledge_base_with_data):
        """Test that text search includes both title and content."""
        # Search for text in title
        results = knowledge_base_with_data.search_by_text("Development")
        assert len(results) == 1
        assert results[0].title == "Web Development"

        # Search for text in content
        results = knowledge_base_with_data.search_by_text("frameworks")
        assert len(results) == 1
        assert results[0].title == "Web Development"

    def test_search_empty_tags_list(self, knowledge_base_with_data):
        """Test search with empty tags list returns all nodes."""
        results = knowledge_base_with_data.search_by_tags([])
        assert len(results) == 4

    def test_search_empty_text_returns_all(self, knowledge_base_with_data):
        """Test search with empty text returns all nodes."""
        results = knowledge_base_with_data.search_by_text("")
        assert len(results) == 4
