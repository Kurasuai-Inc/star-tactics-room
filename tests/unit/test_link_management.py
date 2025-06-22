"""Tests for link management functionality in KnowledgeBase."""

import pytest
from star_tactics.models.knowledge_node import KnowledgeBase


class TestLinkManagement:
    """Test link management operations for KnowledgeBase."""

    @pytest.fixture
    def knowledge_base(self):
        """Provide a fresh KnowledgeBase instance."""
        return KnowledgeBase()

    def test_validate_links_all_valid(self, knowledge_base):
        """Test link validation when all links are valid."""
        # Create nodes
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(title="Node 2", content="Content 2")
        node3_id = knowledge_base.create_node(
            title="Node 3", content="Content 3", links=[node1_id, node2_id]
        )

        # Validate links
        is_valid = knowledge_base.validate_links(node3_id)
        assert is_valid is True

    def test_validate_links_with_invalid(self, knowledge_base):
        """Test link validation when some links are invalid."""
        # Create nodes
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(
            title="Node 2", content="Content 2", links=[node1_id, "invalid-node-id"]
        )

        # Validate links
        is_valid = knowledge_base.validate_links(node2_id)
        assert is_valid is False

    def test_validate_links_nonexistent_node(self, knowledge_base):
        """Test link validation for nonexistent node."""
        is_valid = knowledge_base.validate_links("nonexistent-id")
        assert is_valid is False

    def test_get_broken_links(self, knowledge_base):
        """Test getting broken links from a node."""
        # Create nodes
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(
            title="Node 2",
            content="Content 2",
            links=[node1_id, "broken-link-1", "broken-link-2"],
        )

        # Get broken links
        broken_links = knowledge_base.get_broken_links(node2_id)
        assert len(broken_links) == 2
        assert "broken-link-1" in broken_links
        assert "broken-link-2" in broken_links

    def test_get_broken_links_all_valid(self, knowledge_base):
        """Test getting broken links when all are valid."""
        # Create nodes
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(title="Node 2", content="Content 2")
        node3_id = knowledge_base.create_node(
            title="Node 3", content="Content 3", links=[node1_id, node2_id]
        )

        # Get broken links
        broken_links = knowledge_base.get_broken_links(node3_id)
        assert len(broken_links) == 0

    def test_add_bidirectional_link(self, knowledge_base):
        """Test adding bidirectional links between nodes."""
        # Create nodes
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(title="Node 2", content="Content 2")

        # Add bidirectional link
        success = knowledge_base.add_bidirectional_link(node1_id, node2_id)
        assert success is True

        # Check both nodes have links to each other
        node1 = knowledge_base.get_node(node1_id)
        node2 = knowledge_base.get_node(node2_id)

        assert node2_id in node1.links
        assert node1_id in node2.links

    def test_add_bidirectional_link_existing_link(self, knowledge_base):
        """Test adding bidirectional link when one already exists."""
        # Create nodes with one existing link
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(
            title="Node 2",
            content="Content 2",
            links=[node1_id],  # Already linked to node1
        )

        # Add bidirectional link
        success = knowledge_base.add_bidirectional_link(node1_id, node2_id)
        assert success is True

        # Check both nodes have links to each other
        node1 = knowledge_base.get_node(node1_id)
        node2 = knowledge_base.get_node(node2_id)

        assert node2_id in node1.links
        assert node1_id in node2.links
        # Ensure no duplicate links
        assert node2.links.count(node1_id) == 1

    def test_add_bidirectional_link_invalid_node(self, knowledge_base):
        """Test adding bidirectional link with invalid node."""
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")

        # Try to add link with nonexistent node
        success = knowledge_base.add_bidirectional_link(node1_id, "invalid-id")
        assert success is False

        success = knowledge_base.add_bidirectional_link("invalid-id", node1_id)
        assert success is False

    def test_remove_bidirectional_link(self, knowledge_base):
        """Test removing bidirectional links between nodes."""
        # Create nodes with bidirectional links
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(title="Node 2", content="Content 2")
        knowledge_base.add_bidirectional_link(node1_id, node2_id)

        # Remove bidirectional link
        success = knowledge_base.remove_bidirectional_link(node1_id, node2_id)
        assert success is True

        # Check both nodes no longer have links to each other
        node1 = knowledge_base.get_node(node1_id)
        node2 = knowledge_base.get_node(node2_id)

        assert node2_id not in node1.links
        assert node1_id not in node2.links

    def test_get_all_broken_links(self, knowledge_base):
        """Test getting all broken links in the knowledge base."""
        # Create nodes with various broken links
        node1_id = knowledge_base.create_node(
            title="Node 1", content="Content 1", links=["broken-1", "broken-2"]
        )
        node2_id = knowledge_base.create_node(
            title="Node 2",
            content="Content 2",
            links=["broken-2", "broken-3"],  # broken-2 appears in both
        )
        node3_id = knowledge_base.create_node(
            title="Node 3",
            content="Content 3",
            links=[node1_id, node2_id],  # All valid links
        )

        # Get all broken links
        all_broken = knowledge_base.get_all_broken_links()

        assert len(all_broken) == 2  # Two nodes with broken links
        assert node1_id in all_broken
        assert node2_id in all_broken
        assert node3_id not in all_broken

        # Check the broken links details
        assert set(all_broken[node1_id]) == {"broken-1", "broken-2"}
        assert set(all_broken[node2_id]) == {"broken-2", "broken-3"}

    def test_fix_broken_links(self, knowledge_base):
        """Test fixing broken links by removing them."""
        # Create node with broken links
        node_id = knowledge_base.create_node(
            title="Node", content="Content", links=["valid-id", "broken-1", "broken-2"]
        )

        # Create a valid target node
        valid_id = knowledge_base.create_node(title="Valid", content="Valid content")
        knowledge_base.update_node(node_id, links=[valid_id, "broken-1", "broken-2"])

        # Fix broken links
        removed_count = knowledge_base.fix_broken_links(node_id)
        assert removed_count == 2

        # Check that only valid links remain
        node = knowledge_base.get_node(node_id)
        assert len(node.links) == 1
        assert valid_id in node.links
        assert "broken-1" not in node.links
        assert "broken-2" not in node.links
