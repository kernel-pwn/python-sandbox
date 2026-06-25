import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(23, 59, 59)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("target datetime has passed")
else:
    print("target datetime has not passed")