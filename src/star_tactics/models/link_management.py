"""Link management functionality for KnowledgeBase."""

from datetime import datetime


def validate_links(self, node_id: str) -> bool:
    """Validate that all links in a node point to existing nodes.
    
    Args:
        node_id: The ID of the node to validate
        
    Returns:
        True if all links are valid, False otherwise
    """
    node = self.get_node(node_id)
    if not node:
        return False
    
    # Check if all linked nodes exist
    for link_id in node.links:
        if link_id not in self._nodes:
            return False
    
    return True


def get_broken_links(self, node_id: str) -> list[str]:
    """Get list of broken links from a node.
    
    Args:
        node_id: The ID of the node to check
        
    Returns:
        List of invalid link IDs
    """
    node = self.get_node(node_id)
    if not node:
        return []
    
    broken_links = []
    for link_id in node.links:
        if link_id not in self._nodes:
            broken_links.append(link_id)
    
    return broken_links


def add_bidirectional_link(self, node1_id: str, node2_id: str) -> bool:
    """Add bidirectional links between two nodes.
    
    Args:
        node1_id: First node ID
        node2_id: Second node ID
        
    Returns:
        True if links were added successfully, False otherwise
    """
    node1 = self.get_node(node1_id)
    node2 = self.get_node(node2_id)
    
    if not node1 or not node2:
        return False
    
    # Add link from node1 to node2 if not already present
    if node2_id not in node1.links:
        node1.links.append(node2_id)
        node1.updated_at = datetime.now()
    
    # Add link from node2 to node1 if not already present
    if node1_id not in node2.links:
        node2.links.append(node1_id)
        node2.updated_at = datetime.now()
    
    # Save to storage if available
    if self._storage:
        self._storage.save(self)
    
    return True


def remove_bidirectional_link(self, node1_id: str, node2_id: str) -> bool:
    """Remove bidirectional links between two nodes.
    
    Args:
        node1_id: First node ID
        node2_id: Second node ID
        
    Returns:
        True if links were removed successfully, False otherwise
    """
    node1 = self.get_node(node1_id)
    node2 = self.get_node(node2_id)
    
    if not node1 or not node2:
        return False
    
    # Remove link from node1 to node2
    if node2_id in node1.links:
        node1.links.remove(node2_id)
        node1.updated_at = datetime.now()
    
    # Remove link from node2 to node1
    if node1_id in node2.links:
        node2.links.remove(node1_id)
        node2.updated_at = datetime.now()
    
    return True


def get_all_broken_links(self) -> dict[str, list[str]]:
    """Get all broken links in the knowledge base.
    
    Returns:
        Dictionary mapping node IDs to their broken link IDs
    """
    all_broken = {}
    
    for node_id in self._nodes:
        broken_links = self.get_broken_links(node_id)
        if broken_links:
            all_broken[node_id] = broken_links
    
    return all_broken


def fix_broken_links(self, node_id: str) -> int:
    """Remove broken links from a node.
    
    Args:
        node_id: The ID of the node to fix
        
    Returns:
        Number of broken links removed
    """
    node = self.get_node(node_id)
    if not node:
        return 0
    
    broken_links = self.get_broken_links(node_id)
    if not broken_links:
        return 0
    
    # Remove broken links
    for broken_id in broken_links:
        node.links.remove(broken_id)
    
    node.updated_at = datetime.now()
    return len(broken_links)


# Import and extend KnowledgeBase with link management methods
from .knowledge_node import KnowledgeBase

# Add methods to KnowledgeBase
KnowledgeBase.validate_links = validate_links  # type: ignore[attr-defined]
KnowledgeBase.get_broken_links = get_broken_links  # type: ignore[attr-defined]
KnowledgeBase.add_bidirectional_link = add_bidirectional_link  # type: ignore[attr-defined]
KnowledgeBase.remove_bidirectional_link = remove_bidirectional_link  # type: ignore[attr-defined]
KnowledgeBase.get_all_broken_links = get_all_broken_links  # type: ignore[attr-defined]
KnowledgeBase.fix_broken_links = fix_broken_links  # type: ignore[attr-defined]