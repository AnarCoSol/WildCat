import sys
import os

path = __file__
try:
    if not sys.path.count(path):
        sys.path.append(os.path.dirname(path))

except:
    raise
