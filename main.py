from icalendar import Calendar, Event, Timezone, TimezoneStandard
from datetime import datetime, timedelta
import uuid


# 添加事件
def create_event(summary, start, end, label):
    event = Event()
    event.add('SUMMARY;LANGUAGE=zh_CN', f'{summary}（{label}）')
    event.add('dtstart', start)
    event.add('dtend', end)
    # UID保证唯一
    event['uid'] = str(uuid.uuid1())
    return event


def create_work_event(summary, start, end):
    event = create_event(summary, start, end, "补")
    event.add("TRANSP", "TRANSPARENT")
    event.add("X-APPLE-SPECIAL-DAY", "ALTERNATE-WORKDAY")
    event.add("X-APPLE-UNIVERSAL-ID", str(uuid.uuid1()))
    return event


def create_holiday_event(summary, start, end):
    event = create_event(summary, start, end, "休")
    event.add("TRANSP", "TRANSPARENT")
    event.add("X-APPLE-SPECIAL-DAY", "WORK-HOLIDAY")
    event.add("X-APPLE-UNIVERSAL-ID", str(uuid.uuid1()))
    return event


# Create calendar
cal = Calendar()

cal.add("CALSCALE", "GREGORIAN")
cal.add("X-WR-CALNAME", "温医一院")
cal.add("X-APPLE-LANGUAGE", "zh")
cal.add("X-APPLE-REGION", "CN")
# 北京时间
timezone = Timezone()
timezone.add('tzid', 'Asia/Shanghai')
tz_standard = TimezoneStandard()
tz_standard.add('tzname', 'CST')
tz_standard.add('dtstart', datetime(1970, 1, 1, 0, 0, 0))
tz_standard.add('tzoffsetfrom', timedelta(hours=8))
tz_standard.add('tzoffsetto', timedelta(hours=8))
timezone.add_component(tz_standard)
cal.add_component(timezone)

year = 2024

am_start_h = 8
am_start_m = 0
am_end_h = 12
am_end_m = 0

pm_start_h = 13
pm_start_m = 30
pm_end_h = 16
pm_end_m = 30

# 元旦

# 春节


# 清明节


# 劳动节


# 端午节

# 中秋节


# 国庆节
# 假期：默认全天事件，从当天的 00:00 到次日 00:00 结束。
cal.add_component(create_holiday_event('国庆节假期', datetime(year, 10, 1), datetime(year, 10, 4)))

# 上班安排：具体的上班时间设置为 8:00 至 16:30，或根据实际需要修改时间。
cal.add_component(create_work_event('上班', datetime(year, 9, 30, am_start_h, am_start_m),
                                    datetime(year, 9, 30, pm_end_h, pm_end_m)))

with open(f'wyyy_schedule_{year}.ics', 'wb') as f:
    f.write(cal.to_ical())
