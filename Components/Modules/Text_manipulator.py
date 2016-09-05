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

from status_bar import Status_bar

class Text_manipulator():
        def __init__(self):
                self.file = str()
                self.text = str()
                self.len_input = 1
                self.sb = Status_bar()
                self.silent = False
                
        def Write_new(self,t_file, text):
                f = open(t_file, 'w')
                f.write(text)
                f.close

        def Read_old(self, t_file):
                try:
                        f = open(t_file, 'r')
                        text = f.read()
                        f.close
                except:
                        raise
                
        def Read(self,t_file):
                try:
                        f = open(t_file, 'r')
                        text = f.read()
                        f.close

                except IOError:
                        
                        try:
                                self.Write_new(t_file, str())

                                text = self.Read(t_file)
                                
                        except:
                                raise
                        
                except:
                        raise

                
                return text

        def Change_lines(self, t_file, segments = dict()):#segments = line_no:line
                try:
                        try:
                                text = self.Read(t_file).split("\n")
                        except:
                                text = list()
                                
                        for key in segments.keys:
                                if key > len(text):
                                        for x in range(key - len(text) -1):
                                                text.append(str())

                                        text.append(segments[key])
                                else:
                                        text[key] = segments[key]

                        new_text = str()
                        for t in text: new_text += (t + "\n")
                        
                        self.Write_new(t_file, new_text[:-1])
                                        
                                                
                                
                except:
                        raise
        def Read_lines(self, t_file, segments = list()):#segments = [[int1,int2]]
                try:
                        f = open(t_file, 'r')
                        text = list()
                        for okazaki in segments:
                                for line in f[okazaki[0]:okazaki[1]]:
                                        text.append(line) #line mantain the nl char
                        return text
                                
                except:
                        raise
        
        def Write_add(self,t_file, text):
                old = self.Read(t_file)
                text = old + text
                self.Write_new(t_file, text)

        def differences(self, str_list = list()):
                str_list.sort(key = len)
                for s in str_list:
                        for s in str_list[str_list.index(s):]:
                                pass
                pass
                                        
                
        def Read_as_input_old(self, t_file = str()):
                
                self.sb.comment = "waiting for input in " + str(t_file)
                
                first = True
                while True:
                        if not self.silent:
                                self.sb.rotate()
                                
                        raw = self.Read(t_file).split("\n")
                        if first:
                                first = False
                                self.len_input = len(raw)
                                self.last_line = raw[-1]
                        else:
                                
                                if len(raw) > self.len_input:
                                        #print "len_raw" + str(len(raw))
                                        #print "len_input" + str(self.len_input)
                                        lasts = len(raw) - self.len_input + 1
                                        
                                        self.len_input = len(raw)
                                        self.last_line = raw[-1]
                                        
                                        if len(raw) != 0:                                                
                                                last_lines = str()
                                                for line in raw[-lasts:]: last_lines += line + "\n"
                                                
                                                return last_lines[:-1]
                                elif len(raw) == self.len_input:
                                        if self.last_line != raw[-1]:
                                                self.last_line = raw[-1]
                                                
                                                return self.last_line
                                                
                                        
                                #elif len(raw) < self.len_input:
                                        #self.len_input = len(raw)
        def simple_diff_equal(self, a = str(), b = str()):
                if len(a) == len(b):
                        i = 0
                        new_chars = str()
                        for char in a:
                                if char != b[i]:
                                        new_chars += char
                                i += 1
                                        
                        return new_chars
                
        def simple_diff(self, a = str(), b = str()):
                if a != b:
                        if len(a) > len(b):
                                return self.simple_diff_equal(a[:len(b)], b) + a[len(b):]

                        if len(a) < len(b):
                                pass
                        

                        if len(a) == len(b):
                                return self.simple_diff_equal(a,b)
                else:
                        pass

                return None
                                
                                
                                
                
        def Read_as_input(self, t_file = str()):
                self.sb.comment = "waiting for input in " + str(t_file)
                older = self.Read(t_file)
                while True:
                                
                        result = self.simple_diff(self.Read(t_file), older)
                        if result:
                                return result
                        else:
                                if not self.silent:
                                        self.sb.rotate()
                                
                                        
                                        
        def Write_as_output(self, t_file, text):
                try:
                        self.Write_add(t_file, text)
                except:
                        try:
                                self.Write_new(t_file, text)
                        except:
                                raise

        def Read_and_print(self, t_file):
                while True:
                        try:
                                print self.Read_as_input(t_file)
                        except KeyboardInterrupt:
                                break
                        except:
                                raise
                        
                                
                        
