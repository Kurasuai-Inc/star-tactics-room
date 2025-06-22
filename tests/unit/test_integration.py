"""Integration tests for KnowledgeBase with storage."""

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
from star_tactics.models.knowledge_node import KnowledgeBase
from star_tactics.storage import JSONStorage


class TestKnowledgeBaseWithStorage:
    """Test KnowledgeBase with storage integration."""

    @pytest.fixture
    def temp_dir(self):
        """Provide a temporary directory for testing."""
        with TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    @pytest.fixture
    def kb_with_storage(self, temp_dir):
        """Provide a KnowledgeBase with JSON storage."""
        filepath = temp_dir / "test_kb.json"
        storage = JSONStorage(filepath)
        return KnowledgeBase(storage=storage), filepath

    def test_auto_save_on_create(self, kb_with_storage):
        """Test that nodes are automatically saved on creation."""
        kb, filepath = kb_with_storage

        # Create a node
        node_id = kb.create_node(
            title="Auto Save Test", content="This should be saved automatically"
        )

        # Check file exists
        assert filepath.exists()

        # Load in new KB and verify
        new_kb = KnowledgeBase()
        storage = JSONStorage(filepath)
        storage.load(new_kb)

        node = new_kb.get_node(node_id)
        assert node is not None
        assert node.title == "Auto Save Test"

    def test_auto_save_on_update(self, kb_with_storage):
        """Test that updates are automatically saved."""
        kb, filepath = kb_with_storage

        # Create and update a node
        node_id = kb.create_node(title="Original", content="Original content")
        kb.update_node(node_id, title="Updated")

        # Load in new KB and verify
        new_kb = KnowledgeBase()
        storage = JSONStorage(filepath)
        storage.load(new_kb)

        node = new_kb.get_node(node_id)
        assert node.title == "Updated"

    def test_auto_save_on_delete(self, kb_with_storage):
        """Test that deletions are automatically saved."""
        kb, filepath = kb_with_storage

        # Create and delete a node
        node_id = kb.create_node(title="To Delete", content="Delete me")
        kb.delete_node(node_id)

        # Load in new KB and verify
        new_kb = KnowledgeBase()
        storage = JSONStorage(filepath)
        storage.load(new_kb)

        node = new_kb.get_node(node_id)
        assert node is None

    def test_auto_load_on_init(self, temp_dir):
        """Test that data is automatically loaded on initialization."""
        filepath = temp_dir / "test_kb.json"
        storage = JSONStorage(filepath)

        # Create KB and add data
        kb1 = KnowledgeBase(storage=storage)
        node_id = kb1.create_node(title="Persistent", content="Should persist")

        # Create new KB with same storage
        kb2 = KnowledgeBase(storage=storage)

        # Should have the data
        node = kb2.get_node(node_id)
        assert node is not None
        assert node.title == "Persistent"
