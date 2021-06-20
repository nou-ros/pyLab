import datetime

today = datetime.date.today()
# print(today)
'''
Sunday 6
Monday 0
'''
# print(today.weekday())
'''
Sunday 7
Monday 1
'''
# print(today.isoweekday())

# to print the date of 7 days after today
timedelta = datetime.timedelta(days=7)
# print(today + timedelta)
# to print the date of 7 days before today
# print(today - timedelta)

bday = datetime.date(2021, 11, 15)
till_bday = bday - today
# print("Days remain before my birth date: ", till_bday)
# print("Days remain before my birth date: ", till_bday.days)
# print("Days remain before my birth date: ", till_bday.total_seconds())

# datetime.time only deals with hour, minutes and seconds
t2 = datetime.time(9, 30, 45, 1009)
# print(t2)
# print(t2.hour)

t3 = datetime.datetime(2021, 7, 26, 12, 30, 45, 100000)
# print(t3)


# current local datetime with timezone=none
dt_today = datetime.datetime.today()

# current local datetime, we can pass a timezone if we want. if empty acts as the above
dt_now = datetime.datetime.now()

# current utc time with timezone=none
dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# pytz(recommended) third party package for timezone
# pip install pytz
import pytz

tizo_utc = datetime.datetime.now(tz=pytz.UTC)
# print(tizo_utc)

# converting utc to my timezone 
dt_dhaka = tizo_utc.astimezone(pytz.timezone('Asia/Dhaka'))
print(tizo_utc)

# printing all the timezones
# for tz in pytz.all_timezones:
#     print(tz)

loc_time = datetime.datetime.now()
dhaka_tz = pytz.timezone('Asia/Dhaka')
# converting the local time to timezone
dhaka_time = dhaka_tz.localize(loc_time)
# print(dhaka_time)

timeZone_dhaka = datetime.datetime.now(tz=pytz.timezone('Asia/Dhaka'))
print(timeZone_dhaka)

# print in isoformat - check the document
print(timeZone_dhaka.isoformat())
print(timeZone_dhaka.strftime('%B %d, %Y'))

dt_str = 'July 26, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime