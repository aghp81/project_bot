import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.speech_to_text import convert_voice_to_text

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice_file = await update.message.voice.get_file()
    file_path = f"voice_{update.message.message_id}.ogg"
    await voice_file.download_to_drive(file_path)

    # ابتدا تلاش برای فارسی
    text_fa = convert_voice_to_text(file_path, lang="fa-IR")

    # اگر متن خالی بود، تلاش برای انگلیسی
    text_en = ""
    if "نتونستم" in text_fa:
        text_en = convert_voice_to_text(file_path, lang="en-US")

    # پاک کردن فایل اصلی ogg
    if os.path.exists(file_path):
        os.remove(file_path)

    # پاسخ به کاربر
    if text_fa and "نتونستم" not in text_fa:
        await update.message.reply_text(f"🎤 متن ویس شما (فارسی):\n{text_fa}")
    elif text_en and "متاسفم" not in text_en:
        await update.message.reply_text(f"🎤 متن ویس شما (انگلیسی):\n{text_en}")
    else:
        await update.message.reply_text("❌ متاسفم، نتونستم متن ویس رو تشخیص بدم.")
