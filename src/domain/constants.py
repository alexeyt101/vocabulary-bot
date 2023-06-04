"""Common use domain constants."""
from src.domain.messages_texts import (
    GREETINGS_MESSAGE,
    METHOD_HELP_MESSAGE,
)

MESSAGES_BY_KEY: dict[str, str] = {
    'greetings': GREETINGS_MESSAGE,
    'method_help': METHOD_HELP_MESSAGE,
}
