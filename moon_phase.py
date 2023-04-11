import datetime
import pytz
from lunarcalendar import LunarCalendar, MoonPhase

# define ASCII moon phase characters
moon_chars = ['🌑', '🌒', '🌓', '🌔', '🌕', '🌖', '🌗', '🌘']

# get current time in local timezone
local_tz = pytz.timezone('YOUR_TIMEZONE')
now = datetime.datetime.now(local_tz)

# get current moon phase
moon_phase = LunarCalendar().moon_phase(now)
moon_char = moon_chars[int(moon_phase)]

# get previous and next major moon phases
prev_phase = MoonPhase((moon_phase - 1) % 8)
next_phase = MoonPhase((moon_phase + 1) % 8)

# get dates and times of major moon phases
prev_time = LunarCalendar().next_full_moon(now) if prev_phase == MoonPhase.FULL_MOON else LunarCalendar().next_new_moon(now)
next_time = LunarCalendar().next_new_moon(now) if next_phase == MoonPhase.NEW_MOON else LunarCalendar().next_full_moon(now)
prev_date = prev_time.astimezone(local_tz).strftime('%b %d, %Y')
next_date = next_time.astimezone(local_tz).strftime('%b %d, %Y')
prev_time_str = prev_time.astimezone(local_tz).strftime('%I:%M %p')
next_time_str = next_time.astimezone(local_tz).strftime('%I:%M %p')

# print results
print(moon_char)
print('Prev: {} {} at {}'.format(prev_phase.name.lower().title(), prev_date, prev_time_str))
print('Next: {} {} at {}'.format(next_phase.name.lower().title(), next_date, next_time_str))
