"""Bot entrypoint module."""
from telegram.ext import (
    Application,
    ApplicationBuilder,
    BaseHandler,
    CommandHandler,
)

from configs import TELEGRAM_BOT_TOKEN

from src.external.bot_handlers import (
    greetings_handler,
    method_help_handler,
)


def create_application() -> Application:
    """Application factory."""
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    handlers: list[BaseHandler] = [
        CommandHandler('start', greetings_handler),
        CommandHandler('methodhelp', method_help_handler),
    ]

    for handler in handlers:
        application.add_handler(handler)

    return application


if __name__ == '__main__':
    application = create_application()
    application.run_polling()
