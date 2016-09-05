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
import errno

from Text_manipulator import Text_manipulator
from SQL_agent import SQLite_agent
from Info_retriever import Info_retriever
from status_bar import Status_bar
import time

#03/02/16:
#       - added Logger.log_save() func
#       - compatibility bugs fixed
#03/05/16:
#       - add sqlite compatibility
class Logger(Text_manipulator):
    def __init__(self, log_path = os.getcwd(), log_file = str(), log_db = str()):
        self.pid = os.getpid()
        self.log_path = log_path
        self.silent = False
        
        self.logs = list()
        self.max_logs = 10 #int()
        
        if log_file != str():
            self.log_file = log_path + "/" + log_file
            Text_manipulator.__init__(self)
            self.file_saver = True
            
        else:
            self.file_saver = False

        if log_db != str():
            self.log_db = log_path + "/" + log_db #trouble..
            self.sql_logger = SQLite_agent(self.log_db) #os.dirname(self.log_path)
            self.db_saver = True
            
        else:
            self.db_saver = False

        class Log():
            def __init__(self,log_txt):
                    self.log_txt = log_txt
                    self.log_time = time.ctime()
                    self.log_formatted = self.log_format()
                    
                    self.log_str = self.stringize(self.log_formatted)
                    
            def log_format(self):
                status = self.log_txt[:3]
                
                if " {" and "}" in self.log_txt:
                    body = self.log_txt[self.log_txt.find(" {")+2:self.log_txt.find("}")]
                    sub = self.log_txt[3:self.log_txt.find(" {")]
                else:
                    body = str()
                    sub = self.log_txt[3:]
                time = self.log_time
                formatted = self.log_time + " " + self.log_txt + "\n"
                
                return [time, status, sub, body]
            
            def stringize(self, List = list()):
                string = str()
                for tok in List: string += " " + str(tok)
                string += "\n"

                return string

        self.Log = Log

    def log_db_saver(self):
        #reformat the log: date, status, subject, body
        sql_code = "INSERT INTO Logs (Date, Status, Subject, Body) VALUES ("
        for value in self.logs[-1].log_formatted:
            sql_code += ('"' + value + '",')
        sql_code = sql_code[:-1]
        sql_code += ");"
            
        #print sql_code
        
        self.sql_logger.man_ol_if(sql_code)
        
    def log_db_create(self):
        pass
        
    def log_maker(self,log_txt):
                        
            log = self.Log(log_txt)
            return log
                                  
    def log_txt_saver(self):
            if self.logs != list(): 
                try:
                        self.Write_add(self.log_file, self.logs[-1].log_str)
                except:
                        self.Write_new(self.log_file, self.logs[-1].log_str)
                return True
            
            return False
        
    def log_printer(self):
        if self.logs != list():
            print "\n" + self.logs[-1].log_str

            return True
        
        return False
            
    def log_save(self, log_txt):
        try:
            self.logs.append(self.log_maker(log_txt))
            
            if self.db_saver:
                try:
                    self.log_db_saver()
                except:
                    pass #<- or it can print the precise error if not silent maybe
                
            if self.file_saver:
                try:
                    self.log_txt_saver()
                except:
                    pass #<- or it can print the precise error if not silent maybe

            if not self.silent:
                try:
                    self.log_printer()
                except:
                    print "[-] Extreme error!"#<- or it can print the precise error
                
            
            if len(self.logs) == self.max_logs:
                self.logs = list()
        except:
            print "[-] Extreme error!"#<- same as upcomments
        
    def __meta_logger__(self, l_f = str(), l_db = str(), pid = str(), t = 1, condition = "[+] Running"):
        
        self.Logger = Logger(log_file = l_f, log_db = l_db)
        
        self.ir = Info_retriever()
        s_bar = Status_bar(comment = pid + " program running")
            
        while True:
            try:
                status = self.ir.check_if_alive(pid)
                if status != condition:
                    self.Logger.log_save(status)
                    break
                
                if not self.silent:       
                    s_bar.rotate()
                    
                time.sleep(int(t))
                
                    
                    
            except KeyboardInterrupt:
                exit()
                
            except EOFError:
                pass
                
if __name__ == "__main__":
    args = sys.argv
    L = Logger()

    if len(args) == 3:
        L.__meta_logger__(pid = args[2])
        
    else:
        print ("""usage: python Logger.py [options]
                    options available:
                    -p [pid] <- check if (by pid) program is alive and exit
                    -pw [pid] <- wait in loop then make a log if the program (by pid) is dead
                """)
