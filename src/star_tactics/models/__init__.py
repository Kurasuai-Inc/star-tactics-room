"""データモデルパッケージ"""

from .knowledge_node import KnowledgeNode, KnowledgeBase
from . import link_management as _link_management  # noqa: F401 - Import to register link management methods

__all__ = ["KnowledgeNode", "KnowledgeBase"]
