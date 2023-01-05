from datetime import date
from datetime import timedelta
ans = date.today() - timedelta(days = 5)
print('Date today:',date.today())
print('5 days before:',ans)