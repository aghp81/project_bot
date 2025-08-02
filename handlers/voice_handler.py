from telegram import Update
from telegram.ext import ContextTypes

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("پیام صوتی شما دریافت شد ✅")
