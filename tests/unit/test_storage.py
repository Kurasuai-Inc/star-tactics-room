"""Tests for storage backend functionality."""

import pytest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from star_tactics.storage import StorageBackend, JSONStorage
from star_tactics.models.knowledge_node import KnowledgeBase


class TestStorageBackend:
    """Test the abstract StorageBackend interface."""

    def test_storage_backend_is_abstract(self):
        """Test that StorageBackend cannot be instantiated."""
        with pytest.raises(TypeError):
            StorageBackend()


class TestJSONStorage:
    """Test JSON storage implementation."""

    @pytest.fixture
    def temp_dir(self):
        """Provide a temporary directory for testing."""
        with TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    @pytest.fixture
    def json_storage(self, temp_dir):
        """Provide a JSONStorage instance with temp file."""
        filepath = temp_dir / "test_knowledge_base.json"
        return JSONStorage(filepath)

    @pytest.fixture
    def knowledge_base_with_data(self):
        """Provide a KnowledgeBase with sample data."""
        kb = KnowledgeBase()

        # Add test nodes
        node1_id = kb.create_node(
            title="Node 1", content="Content 1", tags=["tag1", "tag2"]
        )

        kb.create_node(
            title="Node 2", content="Content 2", tags=["tag2", "tag3"], links=[node1_id]
        )

        return kb

    def test_save_empty_knowledge_base(self, json_storage):
        """Test saving an empty knowledge base."""
        kb = KnowledgeBase()
        json_storage.save(kb)

        # Check file was created
        assert json_storage.filepath.exists()

        # Check content
        with open(json_storage.filepath) as f:
            data = json.load(f)

        assert data == {"nodes": {}}

    def test_save_knowledge_base_with_nodes(
        self, json_storage, knowledge_base_with_data
    ):
        """Test saving a knowledge base with nodes."""
        json_storage.save(knowledge_base_with_data)

        # Check file was created
        assert json_storage.filepath.exists()

        # Check content structure
        with open(json_storage.filepath) as f:
            data = json.load(f)

        assert "nodes" in data
        assert len(data["nodes"]) == 2

        # Check node structure
        for node_id, node_data in data["nodes"].items():
            assert "title" in node_data
            assert "content" in node_data
            assert "tags" in node_data
            assert "links" in node_data
            assert "created_at" in node_data
            assert "updated_at" in node_data

    def test_load_empty_file(self, json_storage):
        """Test loading from an empty JSON file."""
        # Create empty JSON file
        json_storage.filepath.write_text('{"nodes": {}}')

        kb = KnowledgeBase()
        json_storage.load(kb)

        assert len(kb.get_all_nodes()) == 0

    def test_load_knowledge_base(self, json_storage, knowledge_base_with_data):
        """Test saving and loading preserves data."""
        # Save
        json_storage.save(knowledge_base_with_data)

        # Load into new knowledge base
        new_kb = KnowledgeBase()
        json_storage.load(new_kb)

        # Compare
        original_nodes = knowledge_base_with_data.get_all_nodes()
        loaded_nodes = new_kb.get_all_nodes()

        assert len(loaded_nodes) == len(original_nodes)

        # Check each node
        for original in original_nodes:
            loaded = new_kb.get_node(original.id)
            assert loaded is not None
            assert loaded.title == original.title
            assert loaded.content == original.content
            assert loaded.tags == original.tags
            assert loaded.links == original.links

    def test_load_nonexistent_file(self, json_storage):
        """Test loading from a nonexistent file creates empty knowledge base."""
        kb = KnowledgeBase()
        json_storage.load(kb)

        assert len(kb.get_all_nodes()) == 0

    def test_file_permissions_error(self, temp_dir):
        """Test handling of file permission errors."""
        # This test is platform-specific and might need adjustment
        filepath = temp_dir / "readonly.json"
        filepath.write_text('{"nodes": {}}')
        filepath.chmod(0o444)  # Read-only

        storage = JSONStorage(filepath)
        kb = KnowledgeBase()

        # Should handle permission error gracefully
        with pytest.raises(PermissionError):
            storage.save(kb)
