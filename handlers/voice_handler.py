from telegram import Update
from telegram.ext import ContextTypes

# اگر ویس بفرستی → پیام تأیید ارسال می‌کنه
async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("پیام صوتی شما دریافت شد ✅")
