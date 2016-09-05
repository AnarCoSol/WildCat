import sys
import os
import Modules
from Formatter import Formatter

class Mail2oParser():
    def __init__(self):
        self.tags = ["from:",
                     "to:",
                     "subject:",
                     "body:"]
    
    def Parse(self, data, meta):
        try:
            data_type, istance, prog_name = meta
            f = Formatter()
            
            if data_type == "o":
                self.dicted = f.dictionarize(data, self.tags)
                
                try:
                    data = str(self.dicted["subject:"]) + str(self.dicted["body:"])#error if not exist one of the two?
                except:
                    try:
                        data = self.dicted["subject:"]
                    except:
                        try:
                            data = self.dicted["body:"]

                        except:
                            raise

            elif data_type == "i":
                #if self.dicted exist
                
                splitted = data.split("\n", 1)

                
                self.dicted["subject:"] = splitted[0]
                    
                if len(splitted) != 1:
                    self.dicted["body:"] = splitted[1]
                    
                else:
                    self.dicted["body:"] = ""

                

                return (self.dicted["from:"] + "\n" + #to
                        self.dicted["subject:"] + "\n" + #sub
                        self.dicted["body:"] + "\n" + #body
                        "None" #attach
                        )
                #f.delinefy(data) -> f.linefy("to:self.dicted["from:"] sub:line1 body:lines", " ")
                
            
            return data
        
        except:
            raise
        

P2oParser = Mail2oParser() #mail_client-API.P2oParser <- object instantied

if __name__ == "__main__":
    pass
    
else:
    pass
    
