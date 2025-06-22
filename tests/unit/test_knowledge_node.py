"""Tests for KnowledgeNode model and KnowledgeBase CRUD operations."""

import pytest
from datetime import datetime
from star_tactics.models.knowledge_node import KnowledgeNode, KnowledgeBase


class TestKnowledgeNode:
    """Test KnowledgeNode data model."""

    def test_create_knowledge_node(self):
        """Test creating a basic knowledge node."""
        node = KnowledgeNode(
            title="Test Node", content="This is test content", tags=["test", "example"]
        )

        assert node.id is not None
        assert node.title == "Test Node"
        assert node.content == "This is test content"
        assert node.tags == ["test", "example"]
        assert isinstance(node.created_at, datetime)
        assert isinstance(node.updated_at, datetime)
        assert node.links == []

    def test_knowledge_node_with_links(self):
        """Test creating a knowledge node with links to other nodes."""
        node1 = KnowledgeNode(title="Node 1", content="Content 1")
        node2 = KnowledgeNode(title="Node 2", content="Content 2")

        node3 = KnowledgeNode(
            title="Node 3", content="Content 3", links=[node1.id, node2.id]
        )

        assert len(node3.links) == 2
        assert node1.id in node3.links
        assert node2.id in node3.links

    def test_knowledge_node_default_values(self):
        """Test default values for optional fields."""
        node = KnowledgeNode(title="Minimal Node", content="Minimal content")

        assert node.tags == []
        assert node.links == []
        assert node.created_at == node.updated_at


class TestKnowledgeBaseCRUD:
    """Test CRUD operations for KnowledgeBase."""

    @pytest.fixture
    def knowledge_base(self):
        """Provide a fresh KnowledgeBase instance for each test."""
        return KnowledgeBase()

    def test_create_node(self, knowledge_base):
        """Test creating a node in the knowledge base."""
        node_id = knowledge_base.create_node(
            title="New Node", content="Node content", tags=["tag1", "tag2"]
        )

        assert node_id is not None
        assert isinstance(node_id, str)

    def test_get_node(self, knowledge_base):
        """Test retrieving a node from the knowledge base."""
        # Create a node
        node_id = knowledge_base.create_node(title="Test Node", content="Test content")

        # Retrieve the node
        node = knowledge_base.get_node(node_id)

        assert node is not None
        assert node.id == node_id
        assert node.title == "Test Node"
        assert node.content == "Test content"

    def test_get_nonexistent_node(self, knowledge_base):
        """Test retrieving a node that doesn't exist."""
        node = knowledge_base.get_node("nonexistent-id")
        assert node is None

    def test_update_node(self, knowledge_base):
        """Test updating an existing node."""
        # Create a node
        node_id = knowledge_base.create_node(
            title="Original Title", content="Original content"
        )

        # Update the node
        success = knowledge_base.update_node(
            node_id, title="Updated Title", content="Updated content", tags=["updated"]
        )

        assert success is True

        # Verify the update
        node = knowledge_base.get_node(node_id)
        assert node.title == "Updated Title"
        assert node.content == "Updated content"
        assert node.tags == ["updated"]
        assert node.updated_at > node.created_at

    def test_update_nonexistent_node(self, knowledge_base):
        """Test updating a node that doesn't exist."""
        success = knowledge_base.update_node("nonexistent-id", title="New Title")
        assert success is False

    def test_delete_node(self, knowledge_base):
        """Test deleting a node."""
        # Create a node
        node_id = knowledge_base.create_node(title="To Delete", content="Delete me")

        # Delete the node
        success = knowledge_base.delete_node(node_id)
        assert success is True

        # Verify deletion
        node = knowledge_base.get_node(node_id)
        assert node is None

    def test_delete_nonexistent_node(self, knowledge_base):
        """Test deleting a node that doesn't exist."""
        success = knowledge_base.delete_node("nonexistent-id")
        assert success is False

    def test_node_links_management(self, knowledge_base):
        """Test managing links between nodes."""
        # Create nodes
        node1_id = knowledge_base.create_node(title="Node 1", content="Content 1")
        node2_id = knowledge_base.create_node(title="Node 2", content="Content 2")

        # Create a node with links
        node3_id = knowledge_base.create_node(
            title="Node 3", content="Content 3", links=[node1_id, node2_id]
        )

        node3 = knowledge_base.get_node(node3_id)
        assert len(node3.links) == 2
        assert node1_id in node3.links
        assert node2_id in node3.links

    def test_update_node_partial(self, knowledge_base):
        """Test partial update of a node."""
        # Create a node
        node_id = knowledge_base.create_node(
            title="Original", content="Original content", tags=["tag1", "tag2"]
        )

        # Update only title
        knowledge_base.update_node(node_id, title="New Title")

        node = knowledge_base.get_node(node_id)
        assert node.title == "New Title"
        assert node.content == "Original content"  # Should remain unchanged
        assert node.tags == ["tag1", "tag2"]  # Should remain unchanged
