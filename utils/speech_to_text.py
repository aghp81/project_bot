import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_voice_to_text(file_path, lang="fa-IR"):
    """
    تبدیل ویس تلگرام به متن فارسی یا انگلیسی
    lang = 'fa-IR' برای فارسی
    lang = 'en-US' برای انگلیسی
    """
    recognizer = sr.Recognizer()

    # تغییر فرمت ogg به wav
    wav_path = file_path.replace(".ogg", ".wav")
    AudioSegment.from_ogg(file_path).export(wav_path, format="wav")

    text_result = ""
    try:
        with sr.AudioFile(wav_path) as source:
            audio = recognizer.record(source)
            text_result = recognizer.recognize_google(audio, language=lang)
    except sr.UnknownValueError:
        text_result = "❌ متاسفم، نتونستم ویس رو تشخیص بدم."
    except sr.RequestError:
        text_result = "❌ خطا در اتصال به سرویس تشخیص گفتار."

    # حذف فایل موقت wav
    if os.path.exists(wav_path):
        os.remove(wav_path)

    return text_result
