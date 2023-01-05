import random
from datetime import datetime
s = random.randint(0,59)
date = datetime(2022,12,31,23,59,s)
now = datetime.now()
print('differnce in seconds:', abs(int(date.strftime("%S")) - int(now.strftime("%S"))))