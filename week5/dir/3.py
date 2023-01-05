import pathlib
import os
a = pathlib.Path(input())
if a.exists():
    print(os.listdir(a))
else: print('does not exists')