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

class IP_retriever():
        def __init__(self):
                self.ex_ip = str()
                self.local_ip = str()
                self.ex_IP_websites = ["http://ip.jsontest.com/"] # is still working ?
                self.local_IP_website = "google.com"
        def retrive_ex_ip(self):
                for website in self.ex_IP_websites:
                        data = re.search('"([0-9.]*)"', urllib.urlopen(self.ex_IP_website).read()).group(1)
                        if data != "":
                                break
                return data #if data = '' try with another site
        def retrive_local_ip(self):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect((self.local_IP_website, 0))
                return s.getsockname()[0]
