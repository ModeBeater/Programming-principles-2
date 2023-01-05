from datetime import date
from datetime import timedelta
Yesterday = date.today() - timedelta(days = 1)
tomorrow = date.today() + timedelta(days = 1)
print('Yesterday:', Yesterday)
print('today:',date.today())
print('tomorrow:',tomorrow)