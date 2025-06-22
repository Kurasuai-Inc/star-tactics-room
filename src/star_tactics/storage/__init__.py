"""Storage backend for persisting knowledge base data."""

from abc import ABC, abstractmethod
from pathlib import Path
import json
from ..models.knowledge_node import KnowledgeBase, KnowledgeNode


class StorageBackend(ABC):
    """Abstract base class for storage backends."""

    @abstractmethod
    def save(self, knowledge_base: KnowledgeBase) -> None:
        """Save the knowledge base to storage.

        Args:
            knowledge_base: The knowledge base to save
        """
        pass

    @abstractmethod
    def load(self, knowledge_base: KnowledgeBase) -> None:
        """Load data into the knowledge base from storage.

        Args:
            knowledge_base: The knowledge base to load data into
        """
        pass


class JSONStorage(StorageBackend):
    """JSON file storage backend."""

    def __init__(self, filepath: Path | str):
        """Initialize JSON storage with file path.

        Args:
            filepath: Path to the JSON file
        """
        self.filepath = Path(filepath)

    def save(self, knowledge_base: KnowledgeBase) -> None:
        """Save the knowledge base to a JSON file.

        Args:
            knowledge_base: The knowledge base to save
        """
        # Convert nodes to serializable format
        data: dict[str, dict] = {"nodes": {}}

        for node in knowledge_base.get_all_nodes():
            data["nodes"][node.id] = {
                "title": node.title,
                "content": node.content,
                "tags": node.tags,
                "links": node.links,
                "created_at": node.created_at.isoformat(),
                "updated_at": node.updated_at.isoformat(),
            }

        # Ensure parent directory exists
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

        # Write to file
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self, knowledge_base: KnowledgeBase) -> None:
        """Load data from JSON file into the knowledge base.

        Args:
            knowledge_base: The knowledge base to load data into
        """
        if not self.filepath.exists():
            # No file to load from
            return

        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Clear existing nodes
        for node in knowledge_base.get_all_nodes():
            knowledge_base.delete_node(node.id)

        # Load nodes
        nodes_data = data.get("nodes", {})

        # Create all nodes - reuse original IDs to maintain links
        for node_id, node_data in nodes_data.items():
            node = KnowledgeNode(
                id=node_id,
                title=node_data["title"],
                content=node_data["content"],
                tags=node_data.get("tags", []),
                links=node_data.get("links", []),
            )
            # Directly add to knowledge base's internal storage
            knowledge_base._nodes[node_id] = node


__all__ = ["StorageBackend", "JSONStorage"]
