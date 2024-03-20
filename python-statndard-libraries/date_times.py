from datetime import datetime, timedelta
import time

dt1 = datetime(2018, 1, 3) + timedelta(days=1)
dt2 = datetime.now()
dt1 = datetime.fromtimestamp(time.time())
dt1 = datetime.strptime("2018/1/1", "%Y/%m/%d")
print(dt1)
print(dt2 > dt1)

duration = dt2 - dt1

print(duration.days)
print(duration.total_seconds())
