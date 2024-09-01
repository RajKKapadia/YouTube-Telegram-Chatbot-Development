import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def start(update: Update, context):
    await update.message.reply_text('Welcome! This bot will echo your messages.')


async def help_command(update: Update, context):
    await update.message.reply_text('Send any message and I will echo it back to you.')


async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)


def main():
    application = Application.builder().token(
        os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    application.run_polling()


if __name__ == '__main__':
    main()
