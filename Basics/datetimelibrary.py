import datetime

#print the date and time right now
print("Data and Time right now: ", datetime.datetime.now())

#print the date and time of 20th march 2024 3pm 30mins 45 seconds
print("Date and time of 20th march 2024 3pm 30mins 45 seconds:", datetime.datetime(2024, 3, 20, 15, 30, 45))

#change the format of date and time for data/month/year hour:minute:second
print("Changed format: ", datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

#find the date and time difference btw date(2 march 2024, 12:30pm and 20 march 2024 12:30 am)
date1 = datetime.datetime.now()
date2 = datetime.datetime(2024, 3, 20, 00, 00, 00)
print("Differnce:", date2 - date1)