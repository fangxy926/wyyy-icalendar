from icalendar import Calendar, Event, Timezone, TimezoneStandard
from datetime import datetime, timedelta
import uuid


# 添加事件
def create_event(summary, start, end):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start)
    event.add('dtend', end)
    # UID保证唯一
    event['uid'] = str(uuid.uuid1())
    return event


# Create calendar
cal = Calendar()
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
cal.add_component(create_event('国庆节假期', datetime(year, 10, 1),
                               datetime(year, 10, 3)))
cal.add_component(create_event('上班', datetime(year, 9, 30, am_start_h, am_start_m),
                               datetime(year, 9, 30, pm_end_h, pm_end_m)))
# cal.add_component(create_event('10月12日上班', datetime(year, 10, 12), datetime(year, 10, 13)))

# Save the calendar to a file
with open(f'wyyy_schedule_{year}.ics', 'wb') as f:
    f.write(cal.to_ical())
