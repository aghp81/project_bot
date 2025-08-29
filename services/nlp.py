import dateparser
import re

def extract_event_info(text: str):
    """
    متن رو تحلیل می‌کنه و:
    - تاریخ و ساعت رو تشخیص می‌ده
    - عنوان رویداد رو استخراج می‌کنه
    """
    # تشخیص تاریخ و زمان
    event_date = dateparser.parse(
        text,
        languages=["fa", "en"],
        settings={"PREFER_DATES_FROM": "future"}
    )

    # حذف تاریخ و ساعت احتمالی از متن برای استخراج عنوان
    # ساده‌ترین روش: حذف اعداد و واژه‌های مرتبط
    title = re.sub(r'\d+[:٫٫]?\d*|صبح|عصر|شب|AM|PM|شنبه|یکشنبه|دوشنبه|سه‌شنبه|چهارشنبه|پنجشنبه|جمعه', '', text, flags=re.IGNORECASE)
    title = title.strip()

    return {
        "datetime": event_date,   # شیء datetime یا None
        "title": title if title else "رویداد بدون عنوان",
        "raw_text": text
    }


# تست سریع
if __name__ == "__main__":
    samples = [
        "شنبه ساعت ۱۰ صبح جلسه با تیم فنی برای رفع باگ",
        "Meeting with client tomorrow at 3pm"
    ]

    for s in samples:
        result = extract_event_info(s)
        print(result)
