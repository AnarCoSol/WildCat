import sys
import os
import Modules
from Formatter import Formatter
from tg_client import Tg_client#
class Telegram2oParser():
    def __init__(self):
        self.tags = ["from:",
                     "msg:"]

        self.dicted = dict()

        self.dicted["from:"] = "AnarCoSol"

        self.tg_client = Tg_client("/root/tg")#

    def Parse(self, data, meta):
        try:
            data_type, istance, prog_name = meta
            f = Formatter()

            if data_type == "o":
                self.dicted = f.dictionarize(data, self.tags)

                try:
                    data = self.dicted["msg:"]

                except:
                    raise

            elif data_type == "i":
                data_list = f.listfy(data, "\n")
                if data_list[-1] == str() and data_list != list():
                    data_list.pop()
                    
                data = str()
                for d in data_list:
                    if d != str() or d!= " ":
                        data += (self.dicted["from:"] + "\n" + #to:
                                d + "\n") #msg:
                        try:
                            print "to: " + str(self.dicted["from:"])
                            print "msg: " + str(d)
                            self.tg_client.sender.send_msg(unicode(self.dicted["from:"].replace(" ", ""), "utf-8"),
                                                           unicode(d, "utf-8"))
                        except:
                            try:
                                info = sys.exc_info()
                                print info
                            except:
                                continue

                data = data[:-1]
                #data = str(data_list)#for debugging purpose

            return data
        
        except:
            raise

P2oParser = Telegram2oParser()
        
if __name__ == "__main__":
    pass
    
else:
    pass
