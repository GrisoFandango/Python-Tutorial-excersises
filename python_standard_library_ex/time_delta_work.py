from datetime import datetime, timedelta  # timedelta give back the duration
# adding + timedelta() we can increase the given date
dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
print("total seconds", duration.total_seconds())
