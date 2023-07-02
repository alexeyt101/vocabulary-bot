"""Domain services module."""
from src.domain.constants import MESSAGES_BY_KEY


class MessageService:
    """Service to manage messages."""

    def get_message_by_key(self, key: str) -> str:
        """Return messages by a key."""
        return MESSAGES_BY_KEY[key]


message_service = MessageService()
