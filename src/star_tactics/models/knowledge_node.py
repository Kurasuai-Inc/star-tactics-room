"""Knowledge Node model and CRUD operations for the knowledge base."""

from datetime import datetime
import uuid


class KnowledgeNode:
    """Represents a node in the knowledge base."""

    def __init__(
        self,
        title: str,
        content: str,
        tags: list[str] | None = None,
        links: list[str] | None = None,
        id: str | None = None,
    ):
        """Initialize a KnowledgeNode.

        Args:
            title: The title of the node
            content: The content of the node
            tags: Optional list of tags
            links: Optional list of linked node IDs
            id: Optional ID (generated if not provided)
        """
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.content = content
        self.tags = tags or []
        self.links = links or []
        now = datetime.now()
        self.created_at = now
        self.updated_at = now


class KnowledgeBase:
    """Manages a collection of knowledge nodes."""

    def __init__(self):
        """Initialize an empty knowledge base."""
        self._nodes: dict[str, KnowledgeNode] = {}

    def create_node(
        self,
        title: str,
        content: str,
        tags: list[str] | None = None,
        links: list[str] | None = None,
    ) -> str:
        """Create a new node in the knowledge base.

        Args:
            title: The title of the node
            content: The content of the node
            tags: Optional list of tags
            links: Optional list of linked node IDs

        Returns:
            The ID of the created node
        """
        node = KnowledgeNode(title=title, content=content, tags=tags, links=links)
        self._nodes[node.id] = node
        return node.id

    def get_node(self, node_id: str) -> KnowledgeNode | None:
        """Retrieve a node by ID.

        Args:
            node_id: The ID of the node to retrieve

        Returns:
            The node if found, None otherwise
        """
        return self._nodes.get(node_id)

    def update_node(
        self,
        node_id: str,
        title: str | None = None,
        content: str | None = None,
        tags: list[str] | None = None,
        links: list[str] | None = None,
    ) -> bool:
        """Update an existing node.

        Args:
            node_id: The ID of the node to update
            title: Optional new title
            content: Optional new content
            tags: Optional new tags (replaces existing)
            links: Optional new links (replaces existing)

        Returns:
            True if the node was updated, False if not found
        """
        node = self._nodes.get(node_id)
        if not node:
            return False

        if title is not None:
            node.title = title
        if content is not None:
            node.content = content
        if tags is not None:
            node.tags = tags
        if links is not None:
            node.links = links

        node.updated_at = datetime.now()
        return True

    def delete_node(self, node_id: str) -> bool:
        """Delete a node from the knowledge base.

        Args:
            node_id: The ID of the node to delete

        Returns:
            True if the node was deleted, False if not found
        """
        if node_id in self._nodes:
            del self._nodes[node_id]
            return True
        return False
