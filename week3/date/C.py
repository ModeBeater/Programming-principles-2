from datetime import date
from datetime import datetime
ans = datetime.now()
now = date.today()
print(now, ans.strftime("%X"))