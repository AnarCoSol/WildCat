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
import time

#changelog:
#
#03/02/16:
#       - add Messenger.sender func
#       - compatibility bugs fixed
#04/02/16:
#       - exported from this module the status_bar code, now implemented in a class in status_bar.py module
#18/05/16;
#       - add logs on receive() for debugging
#       - migrated Message() from receive() to __init__() <- WARNING: with this change, now receive() is dependent to __init__()! need some adj i.e. self.Msg = Message
#02/05/16:
#       - now it can attach multiple files
from Text_manipulator import Text_manipulator
from status_bar import Status_bar
class Messenger():
        def __init__(self, data_path = os.getcwd() + "/Data"):
                self.silent = False
                self.username = str()
                self.password = str()
                self.mail_to = str()
                self.messages = list()
                self.t_m = Text_manipulator()
                self.data_path = data_path
                self.input_path = os.getcwd() + "/input_path.txt"
                self.head_status = os.getcwd() + "/head_status.txt"
                #----------------------Message class---------------------------------
                class Message():
                        def __init__(self, msg_coded):
                                #Attachements[n].name for the path plus name of the file saved
                                self.msg_coded = msg_coded
                                self.From,self.To,self.Date,self.Message_ID,self.Subject,self.Body,self.Attachements,self.Formatted = self.fetch_infos()

                        def fetch_infos(self):
                                From = str()
                                To = str()
                                Date = str()
                                Message_ID = str()
                                Subject = str()
                                Body = str()
                                Attachements = list()
                                for part in self.msg_coded.walk():
                                        if part.get("From",None) != None:
                                                From = part.get("From",None)
                                        if part.get("To",None) != None:
                                                To = part.get("To",None)
                                        if part.get("Date",None) != None:
                                                Date = part.get("Date",None)
                                        if part.get("Message-ID",None) != None:
                                                Message_ID = part.get("Message-ID",None)
                                        if part.get("Subject",None) != None:
                                                Subject = part.get("Subject",None)
                                        else:
                                                if part.get("Content-Type",None) == 'text/plain; charset=UTF-8' or part.get("Content-Type",None) == 'text/plain; charset="us-ascii"':
                                                        Body = part.get_payload(decode=True)
                                                else:
                                                        Attachements = self.fetch_attachments()
                                                        
                                #format the message for simple and unitary reading
                                Formatted = "Message-ID: " + Message_ID
                                Formatted +="\nDate: " + Date
                                Formatted +="\nfrom: " + From
                                Formatted +="\nto: " + To
                                Formatted +="\nsubject: " + Subject
                                Formatted +="\nbody:\n" + Body
                                Formatted +="\nattachements:\n"
                                for attachement in Attachements:
                                        try:
                                                Formatted += attachement.name
                                        except:
                                                Formatted += "\n"
                                        Formatted += "\n"
                                        
                                        
                                return From, To, Date, Message_ID, Subject, Body, Attachements, Formatted
                                
                        def fetch_attachments(self,path_to_save = os.getcwd()):
                                
                                class Attachement(object):
                                        def __init__(self):
                                                self.data = None
                                                self.content_type = None
                                                self.size = None
                                                self.name = None
                                                
                                def parse_attachment(message_part):
                                        content_disposition = message_part.get("Content-Disposition", None)
                                        if content_disposition:
                                                dispositions = content_disposition.strip().split(";")
                                                if bool(content_disposition and dispositions[0].lower() == "attachment"):

                                                        attachment = Attachement()
                                                        attachment.data = message_part.get_payload(decode=True)
                                                        #attachment.content_type = message_part.get_content_type()
                                                        #print attachment.type
                                                        #attachment.size = len(attachment.data)
                                                        #print attachment.size
                                                        attachment.name = message_part.get_filename()

                                                        return attachment

                                        return None
                                
                                path = path_to_save
                                f_list = os.listdir(path)

                                msg = self.msg_coded
                                attachements = list();
                                if(msg.is_multipart()):
                                        for part in msg.walk():
                                                attachement = parse_attachment(part)
                                                if(attachement):
                                                        attachements.append(attachement)
                                for att in attachements:
                                        name = path + "/" + att.name
                                        if att.name not in f_list:
                                                file = open(name, 'w')
                                                file.write(att.data)
                                                file.close()
                                                print att.name + " saved in " + path
                                        else:
                                                print "[!] " + att.name + " already exist in " + path
                                return attachements
                #-------------------------------End Message class-----------------------------------------
                        
                self.Message = Message #message class not istanced
                        
        def sub_logger(self, args):
                #override if "meta-logger" already exist where Messenger() will be implemented
                if self.silent:
                        pass
                else:
                        print args
                        
        def message_saver(self):
                if self.messages != list():
                        for message in self.messages:
                                try:
                                        self.t_m.Write_add(self.data_path, message.Formatted)
                                except:
                                        self.t_m.Write_new(self.data_path, message.Formatted)
        def message_restore(self):
                try:
                        raw = self.t_m.Read(self.data_path)
                except:
                        return list() #(?)
                #decode raw and save the data in a list
                #self.messages.extend(list)
                return #return the list
        def message_display(self):
                for message in messages:
                        break #display filtered messages (only selected infos)  
                        
        def send(self,username,password,mail_to,subject = str(), text = str(), attach = list()):
                msg = MIMEMultipart()
                msg['From'] = username
                msg['To'] = mail_to
                msg['Subject'] = subject

                if text != str():
                        msg.attach(MIMEText(text))

                if attach != list(): #WARN! not tested (02/05/16) from here<-
                        for a in attach:
                                part = MIMEBase('application', 'octet-stream')
                                part.set_payload(open(a, 'rb').read())
                                Encoders.encode_base64(part)
                                part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(a))
                                msg.attach(part) #to here <-
                        
                mailServer = smtplib.SMTP("smtp.gmail.com", 587)
                mailServer.ehlo()
                mailServer.starttls()
                mailServer.ehlo()
                mailServer.login(username,password)
                mailServer.sendmail(username, mail_to, msg.as_string())
                mailServer.close()
                
        def receive(self,username,password):
                #self.sub_logger("[+] receive start") error not from here, ashed
                
                pop_server = poplib.POP3_SSL('pop.gmail.com')
                pop_server.user(username)
                pop_server.pass_(password)
                
                #self.sub_logger("[+] connected with " + username + ", passw: " + password) #error detected from here 
                
                messages = [pop_server.retr(i) for i in range(1, len(pop_server.list()[1]) + 1)]

                #self.sub_logger("[+] messages = [pop_server.retr(i)]")
                
                messages = ["\n".join(mssg[1]) for mssg in messages]

                #self.sub_logger("[+] messages = [messages formatting without new line]")
                
                messages = [parser.Parser().parsestr(mssg) for mssg in messages]

                #self.sub_logger("[+] messages = [messages_parsed(i)]")
                pop_server.quit()

                #self.sub_logger("[+] messages retrieved from server, formatting started") #to here 26/04/16
                                
                msgs_decrypted = list()
                for msg_coded in messages:
                        msg = self.Message(msg_coded)
                        self.messages.append(msg)
                        msgs_decrypted.append(msg)
                return msgs_decrypted

        def remove(self,username,password): #move all the inbox msgs to trashbin
                server = imaplib.IMAP4_SSL("imap.gmail.com")
                server.login(username,password)
                server.select()
                server.store("1:*", '+X-GM-LABELS', '\\Trash')
                server.expunge() #should be useless
                
        def receiver(self, code_appender = list()):
                #self.sub_logger("[+] receiver start") <-unash for more logs
                
                s_bar = Status_bar("receiving")
                
                while code_appender == list():
                        if not self.silent:
                                s_bar.b_comment = " " + time.ctime() + " "
                                s_bar.rotate()
                                
                        code_appender = self.receive(self.username, self.password)
                        
                if code_appender != list() : return code_appender
                
        def sender(self):
                while True:
                        if self.silent:
                                self.Write_add(self.head_status, "\n" + "subject")
                                txt = self.Read_as_input(self.input_path)
                                self.Write_add(self.head_status, "\n" + "body")
                                body = self.Read_as_input(self.input_path)
                                attach = "none"

                                breaking = "n"
                        else:
                                txt = raw_input("[?] subject > ")
                                body = raw_input("[?] body > ")
                                #attach = raw_input("[?] attachement (leave blank if no attach)> ") <- with multi attach this line will be edited
                                if attach == str():
                                        attach = "none"
                                        
                                breaking = raw_input("[?] continue? [Y/n] > ")
                        try:      
                                self.send(self.username, self.password, self.mail_to, txt, body, attach)
                        except:
                                raise
                        if breaking == "n": return False
                        
if __name__ == "__main__":
        m = Messenger()
        m.sender()
        m.receiver
        
#Messenger.save() and Messenger.saver() not implemented yet
#Messenger.sender can be more generic, it can send email use custom id and send to custom address
