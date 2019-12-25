import datetime

from dateutil.tz import tzlocal

dt = datetime.datetime.now(tzlocal())
print(str(dt))

print(datetime.datetime.now().time().strftime('%H:%M'))
