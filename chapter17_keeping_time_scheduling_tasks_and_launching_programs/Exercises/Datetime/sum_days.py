import datetime

dt = datetime.datetime(2018, 12, 2, 18, 38, 50)
delta = datetime.timedelta(days=1000)

print(dt + delta)