from datetime import datetime

now = datetime.now()

# 1
with open('today.txt', 'wt') as fout:
    fout.write(str(now))

# 2
today_string = None
with open('today.txt', 'rt') as fin:
    today_string = fin.read()

print(today_string)

# 3
date = datetime.strptime(today_string, '%Y-%m-%d %H:%M:%S.%f')
print(date)

# 4
import os
print(os.listdir('.'))

# 5
print(os.listdir('..'))

# 6 -> chapter_10_2.py

# 7
from datetime import date
birthday = date(1985, 5, 9)

# 8
print(birthday.weekday())
print(birthday.isoweekday())
import locale
locale.setlocale(locale.LC_TIME, 'ru_ru')
print(birthday.strftime('%A'))

# 9
from datetime import timedelta
one_day = timedelta(days=1)
print(birthday + 10000 * one_day)