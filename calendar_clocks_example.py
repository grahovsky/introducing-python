import calendar

print(calendar.isleap(1900))
print(calendar.isleap(1996))
print(calendar.isleap(1999))
print(calendar.isleap(2000))
print(calendar.isleap(2002))
print(calendar.isleap(2004))

# datetime Module
from datetime import date
halloween = date(2019, 10, 31)
print(halloween.day)
print(halloween.month)
print(halloween.year)
print(halloween.isoformat())

# timedelta
from datetime import timedelta

now = date.today()
print(now)
# 2020-07-01

one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 17 * one_day)
yesterday = now - one_day
print(yesterday)

from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.minute)

from datetime import datetime
some_day = datetime(2020, 1, 2, 3, 4, 5, 6)
print(some_day)
# 2020-01-02 03:04:05.000006

now = datetime.now()
print(now)
# 2020-07-01 19:19:28.088075

print(now.year)
print(now.minute)
print(now.microsecond)

# You can combine() a date object and a time object into a datetime:
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)

# yank the date and time from a datetime by using the date() and time() methods:
print(noon_today.date())
print(noon_today.time())

# Using the time Module
import time
# The time module’s time() function returns the current time as an epoch value:
now = time.time()
print(now)
# 1593620610.3717399
# convert an epoch value to a string by using ctime():
print(time.ctime(now))

print(time.localtime(now))
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=1, tm_hour=19, tm_min=26, tm_sec=8, tm_wday=2, tm_yday=183, tm_isdst=0)
print(time.gmtime(now))
# time.struct_time(tm_year=2020, tm_mon=7, tm_mday=1, tm_hour=16, tm_min=26, tm_sec=44, tm_wday=2, tm_yday=183, tm_isdst=0)

now = time.localtime()
print(now)
print(list(now[x] for x in range(9)))
# [2020, 7, 1, 19, 28, 34, 2, 183, 0]


# mktime() goes in the other direction, converting a struct_time object to epoch seconds:
# tm = time.localtime(now)
# print(time.mktime(tm))

import locale
from datetime import date
halloween = date(2019, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is', 'ru_ru',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))

import locale
names = locale.locale_alias.keys()
good_names = [name for name in names if \
len(name) == 5 and name[2] == '_']

ru = [name for name in good_names if name.startswith('ru')]
print(ru)