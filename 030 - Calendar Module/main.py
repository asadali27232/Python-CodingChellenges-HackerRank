import calendar as cld

cld.setfirstweekday(cld.MONDAY)
m, d, y = map(int, input().split())
print(cld.day_name[cld.weekday(y, m, d)].upper())

print(cld.TextCalendar(firstweekday=0).formatyear(y))
