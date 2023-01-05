import os
import pathlib
a = pathlib.Path(input())
if a.exists():
    print('Existence:', os.access(a, os.F_OK))
    print('path exists')
    os.remove(a)
else: print('path does not exist')