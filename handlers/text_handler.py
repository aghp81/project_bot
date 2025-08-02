from telegram import Update
from telegram.ext import ContextTypes

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"پیام متنی شما دریافت شد:\n{user_message}")
