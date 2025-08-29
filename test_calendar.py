import datetime
from services.calendar_service import create_event

start_time = datetime.datetime(2025, 8, 15, 10, 0)  # 15 آگوست 2025 - ساعت 10 صبح
end_time = start_time + datetime.timedelta(hours=1)

event_link = create_event(
    summary="جلسه با تیم فنی",
    description="بررسی مشکلات اخیر",
    start_time=start_time,
    end_time=end_time
)

print(f"✅ رویداد ایجاد شد: {event_link}")


# یک مرورگر باز میشه، ازت می‌خواد با اکانت گوگل لاگین کنی و به برنامه اجازه دسترسی بدی.