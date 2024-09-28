from icalendar import Calendar, Event
from datetime import datetime, timedelta, timezone
import uuid
import time

# 北京时间
tz_utc_8 = timezone(timedelta(hours=8))


# Function to create an event
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

year = 2024

# 元旦

# 春节


# 清明节


# 劳动节


# 端午节

# 中秋节


# 国庆节
cal.add_component(create_event('国庆节假期', datetime(year, 10, 1, tzinfo=tz_utc_8),
                               datetime(year, 10, 3, tzinfo=tz_utc_8)))
# cal.add_component(create_event('9月29日上班', datetime(year, 9, 29), datetime(year, 9, 30)))
# cal.add_component(create_event('10月12日上班', datetime(year, 10, 12), datetime(year, 10, 13)))

# Save the calendar to a file
with open(f'wyyy_schedule_{year}.ics', 'wb') as f:
    f.write(cal.to_ical())
