from datetime import date, datetime, timedelta

format = "%d/%m/%Y %H:%M"
d1 = datetime.strptime("22/10/2002 13:01", format)
d2 = datetime.strptime("22/10/2001 13:01", format)
print((d1-d2).days)
