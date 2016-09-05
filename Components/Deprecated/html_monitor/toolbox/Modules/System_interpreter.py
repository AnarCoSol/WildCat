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
from cStringIO import StringIO

class System_interpreter():
        def __init__(self):
                self.silent = False
                
                self.params = str()
        def result_printer(self, code = str(), status = "[ ]", result = "[^] result: none"):
                if not self.silent:                      
                        print status + " command executed: " + str(code)
                        print result
                        
        def command(self,params = str()):
                try:
                        proc = subprocess.Popen(params, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        # read output
                        out = proc.stdout.read() + proc.stderr.read()
                        
                        result = "[^] result: " + str(out)
                        stat = "[+]"
                except:
                        out = sys.exc_info()
                        result = "[^] error: " + str(out)
                        stat = "[-]"

                self.result_printer(params, stat, result)
                return out
                        
        def py_command(self, code = str()):
                result = str()
                out = str()
                #try:
                code_r = code.replace("\\n", "\n")

                old_stdout = sys.stdout

                redir_out = sys.stdout = StringIO()
                try:
                        exec str(code_r) in globals(), locals()
                except:
                        out = sys.exc_info()
                        result = "[^] error: " + str(out)
                        stat = "[-]"
                        
                sys.stdout = old_stdout
                
                if out == str():
                        out = redir_out.getvalue()
                        result = "[^] result: " + str(out)
                        stat = "[+]"
                        
                self.result_printer(code, stat, result)
                return out

                        
        def sys_emulator(self):
                while True:
                        cur_path = os.getcwd()
                        print self.command(raw_input("Dark@Hurd:" + cur_path + "# "))

        def py_smemulator(self):
                while True:
                        print self.py_command(str(raw_input(">>> ")))

                
        def py_emulator(self):
                while True:
                        code = raw_input(">>> ")
                                
                        result = str()
                        out = str()
                        #try:
                        code_r = code.replace("\\n", "\n")

                        old_stdout = sys.stdout

                        redir_out = sys.stdout = StringIO()
                        try:
                                exec(str(code_r))
                        except:
                                out = sys.exc_info()
                                result = "[^] error: " + str(out)
                                stat = "[-]"
                                
                        sys.stdout = old_stdout
                        
                        if out == str():
                                out = redir_out.getvalue()
                                result = "[^] result: " + str(out)
                                stat = "[+]"
                                
                        self.result_printer(code, stat, result)
                        print out
                        
                        
if __name__ == "__main__":
        se = System_interpreter()
        if raw_input("python or system emulator? [py/SYS] > ") == "py":
                se.silent = True
                #print python version
                se.py_emulator()
        else:
                se.silent = True
                se.sys_emulator()
        
