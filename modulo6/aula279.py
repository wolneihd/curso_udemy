# https://docs.python.org/3/library/calendar.html
import calendar

print(calendar.month(2024,6))
print(calendar.calendar(2022))
print(calendar.monthrange(2022,12))
print(list(calendar.day_name))
print(calendar.day_name[calendar.weekday(2024,6,26)])
print(calendar.monthcalendar(2024,6))
for week in calendar.monthcalendar(2024,6):
    print(week)