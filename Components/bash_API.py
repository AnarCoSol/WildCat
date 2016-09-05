import sys
import os
import Modules
from Formatter import Formatter

class Bash2oParser():
    def __init__(self):
        pass
    
    def Parse(self, data, meta):
        try:
            data_type, istance, prog_name = meta
            f = Formatter()
            
            if data_type == "o":
                #data = f.delinefy(data)
                pass
            
            if data_type == "i":
                pass
            
            return data
        
        except:
            raise
        

P2oParser = Bash2oParser() #bash-API.P2oParser <- object instantied

if __name__ == "__main__":
    pass
    
else:
    pass
    
