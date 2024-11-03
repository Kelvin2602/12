import logging
from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN
from src.handlers import (
    start_command,
    start_shift,
    end_shift,
    start_break,
    end_break
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    # Create the Updater
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start_shift", start_shift))
    dp.add_handler(CommandHandler("end_shift", end_shift))
    dp.add_handler(CommandHandler("break", start_break))
    dp.add_handler(CommandHandler("end_break", end_break))

    # Start the Bot
    updater.start_polling()
    logger.info("Bot started successfully!")

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()