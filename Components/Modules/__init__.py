import sys
import os

__author__ = "AnarCoSol"
__credits__ = "part of The Wild/Cat reimplementation of Operator project"
__license__ = "Free as Anarchist Freedom"

path = __file__
try:
    if not sys.path.count(path):
        sys.path.append(os.path.dirname(path))

except:
    raise
 
