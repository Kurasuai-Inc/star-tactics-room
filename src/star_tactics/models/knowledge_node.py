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

    def __init__(self, storage=None):
        """Initialize an empty knowledge base.

        Args:
            storage: Optional storage backend for persistence
        """
        self._nodes: dict[str, KnowledgeNode] = {}
        self._storage = storage

        # Load from storage if provided
        if self._storage:
            self._storage.load(self)

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

        # Save to storage if available
        if self._storage:
            self._storage.save(self)

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

        # Save to storage if available
        if self._storage:
            self._storage.save(self)

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

            # Save to storage if available
            if self._storage:
                self._storage.save(self)

            return True
        return False

    def search_by_tags(self, tags: list[str]) -> list[KnowledgeNode]:
        """Search nodes by tags (AND search).

        Args:
            tags: List of tags to search for

        Returns:
            List of nodes that have all specified tags
        """
        if not tags:
            return list(self._nodes.values())

        # Convert search tags to lowercase for case-insensitive search
        search_tags = [tag.lower() for tag in tags]

        results = []
        for node in self._nodes.values():
            # Convert node tags to lowercase for comparison
            node_tags_lower = [tag.lower() for tag in node.tags]
            # Check if all search tags are in node tags
            if all(tag in node_tags_lower for tag in search_tags):
                results.append(node)

        return results

    def search_by_text(self, text: str) -> list[KnowledgeNode]:
        """Search nodes by text in title or content.

        Args:
            text: Text to search for (case-insensitive)

        Returns:
            List of nodes that contain the text in title or content
        """
        if not text:
            return list(self._nodes.values())

        # Convert search text to lowercase for case-insensitive search
        search_text = text.lower()

        results = []
        for node in self._nodes.values():
            # Check if text is in title or content (case-insensitive)
            if search_text in node.title.lower() or search_text in node.content.lower():
                results.append(node)

        return results

    def get_all_nodes(self) -> list[KnowledgeNode]:
        """Get all nodes in the knowledge base.

        Returns:
            List of all nodes
        """
        return list(self._nodes.values())
