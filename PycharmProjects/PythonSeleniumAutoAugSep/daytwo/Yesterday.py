from datetime import datetime,timedelta

today = datetime.now()
print("Today ", today)

one = timedelta(days=1)
yesterday =  today - one
print("Yesterday", yesterday)


tomorrow =  today + one
print("Tomorrow",tomorrow)
