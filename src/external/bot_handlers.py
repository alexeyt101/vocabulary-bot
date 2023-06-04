"""Bot handlers module."""
import logging

from telegram import Update
from telegram.ext import ContextTypes

from src.domain.services import message_service

logger = logging.getLogger(__name__)


async def greetings_handler(update: Update,
                            context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start command handler."""
    message_key = 'greetings'
    effective_chat = update.effective_chat

    if not effective_chat:
        logger.warning('Effective chat is None')
        return

    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=message_service.get_message_by_key(message_key),
    )


async def method_help_handler(update: Update,
                              context: ContextTypes.DEFAULT_TYPE) -> None:
    """90 method help handler."""
    message_key = 'method_help'
    effective_chat = update.effective_chat

    if not effective_chat:
        logger.warning('Effective chat is None')
        return

    await context.bot.send_message(
        chat_id=effective_chat.id,
        text=message_service.get_message_by_key(message_key),
    )
