"""Tests for link management with storage integration."""

import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
from star_tactics.models.knowledge_node import KnowledgeBase
from star_tactics.storage import JSONStorage


class TestLinkManagementWithStorage:
    """Test link management operations with storage persistence."""
    
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
    
    def test_bidirectional_link_persistence(self, kb_with_storage):
        """Test that bidirectional links are persisted to storage."""
        kb, filepath = kb_with_storage
        
        # Create nodes
        node1_id = kb.create_node(title="Node 1", content="Content 1")
        node2_id = kb.create_node(title="Node 2", content="Content 2")
        
        # Add bidirectional link
        success = kb.add_bidirectional_link(node1_id, node2_id)
        assert success is True
        
        # Verify file was updated
        assert filepath.exists()
        
        # Load in new KB and verify links persist
        new_kb = KnowledgeBase(storage=JSONStorage(filepath))
        
        node1 = new_kb.get_node(node1_id)
        node2 = new_kb.get_node(node2_id)
        
        assert node1 is not None
        assert node2 is not None
        assert node2_id in node1.links
        assert node1_id in node2.links
    
    def test_remove_bidirectional_link_persistence(self, kb_with_storage):
        """Test that link removal is persisted to storage."""
        kb, filepath = kb_with_storage
        
        # Create nodes with links
        node1_id = kb.create_node(title="Node 1", content="Content 1")
        node2_id = kb.create_node(title="Node 2", content="Content 2")
        kb.add_bidirectional_link(node1_id, node2_id)
        
        # Remove links
        success = kb.remove_bidirectional_link(node1_id, node2_id)
        assert success is True
        
        # Load in new KB and verify links are removed
        new_kb = KnowledgeBase(storage=JSONStorage(filepath))
        
        node1 = new_kb.get_node(node1_id)
        node2 = new_kb.get_node(node2_id)
        
        assert node2_id not in node1.links
        assert node1_id not in node2.links
    
    def test_fix_broken_links_persistence(self, kb_with_storage):
        """Test that fixing broken links is persisted to storage."""
        kb, filepath = kb_with_storage
        
        # Create node with broken links
        node_id = kb.create_node(
            title="Node with broken links",
            content="Content",
            links=["broken1", "broken2"]
        )
        
        # Fix broken links
        fixed_count = kb.fix_broken_links(node_id)
        assert fixed_count == 2
        
        # Load in new KB and verify broken links are gone
        new_kb = KnowledgeBase(storage=JSONStorage(filepath))
        
        node = new_kb.get_node(node_id)
        assert len(node.links) == 0
        assert "broken1" not in node.links
        assert "broken2" not in node.links