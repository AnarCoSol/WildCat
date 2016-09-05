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
import zipfile
import shutil
import errno

from Text_manipulator import Text_manipulator
from SQL_agent import SQLite_agent

class File_manager():
    def __init__(self):
        self.tm = Text_manipulator()
    def zip_dir(self, dir_to_zip = str(), zip_out = str()):
        def zipdir(path, ziph):
            # ziph is zipfile handle
            f_list = str()
            
            for root, dirs, files in os.walk(path):
                for file in files:
                    ziph.write(os.path.join(root, file))
                    f_list.append(file)
                    
            return f_list
                    
        zipf = zipfile.ZipFile(zip_out, 'w', zipfile.ZIP_DEFLATED)
        
        zipped = zipdir(dir_to_zip, zipf)
        
        zipf.close()
        
        return zipped
        

    def unzip(self, zip_path = str(), dest_path = str()):
        try:
            zip_ref = zipfile.ZipFile(zip_path, 'r')
            zip_ref.extractall(dest_path)
            zip_ref.close()
        except:
            return "[-]" # <--it can be more accurate
        
        return "[+] " + zip_path + " succesfully unziped to " + dest_path

    def copy(self,src = str(), dest = str()):
        try:
            shutil.copytree(src, dest, ignore=shutil.ignore_patterns('*.py', '*.sh', 'specificfile.file'))
        except OSError as e:
            # If the error was caused because the source wasn't a directory
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dest)
                
            else:
                return "[-] " + src + " not copied. Error: %s " % e

        return "[+] " + src + " copied to " + dest


class Tools_manager(File_manager):
    def __init__(self):
        File_manager.__init__(self)

    def search_tools(self, path = str(), line_no = str(),pattern = str(), extension = str()):#pattern = str()
        f_list = os.listdir(path)
        tools = list()
        for f in f_list:
            if f[-len(extension):] == extension:
                line = self.tm.Read_lines(t_file = path + "/" + f,
                                          segments = [[int(line_no)-1, int(line_no)]])

                if line == pattern:
                    tools.append(f)
        return tools
    
    def save_tools_list(self, db_name = str()):
        sql_a = SQLite_agent(db_name)
        
        sql_code = "INSERT INTO Tools (Path, Name) VALUES ("
        for value in values:
            sql_code += ('"' + value + '",')
        sql_code = sql_code[:-1]
        sql_code += ");"

        sql_a.man_ol_if(sql_code)

    def check_avail_tools(self):
        pass
        
        

if __name__ == "__main__":
    pass
