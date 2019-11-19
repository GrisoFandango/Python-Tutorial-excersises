# to do a clearer code we import datetime from datetime,
# so everytime we want to use datetime,
# we do not need to write datetime.datetime
from datetime import datetime
import time
dt2 = datetime(2018, 1, 1)
# print(dt)
# datetime.now shows us current date and time
dt = datetime.now()
print(dt)
# striptime is used to convert a string into datetime object
# and we need to specify how to interpret the string, using %Y,%m,%d
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dt)
# we can convert a time object in datetime object
dt = datetime.fromtimestamp(time.time())
print(dt)
print(f"{dt.day}/{dt.month}/{dt.year}")
# strftime is the opposite of strtime, convert a datetime object into a string
print(dt.strftime("%Y/%m"))
# we can also compare dates
print(dt2 > dt)
