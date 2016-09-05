import os
import sys
import time

from Modules.Messenger import Messenger

from Modules.Text_manipulator import Text_manipulator

from Modules.Thread_launcher import Thread_launcher

import mail_client

import __init__#or itself as import mail_client.__file__
slash = "/" #sketchy
__file__ = os.path.dirname(__init__.__file__) + slash +  __file__.split(slash)[-1]

__usage__ = "python " + __file__  + " [receive/send/Both] -u [user] -p [passwd] -t [receiving refresh time, default: 5 secs]"

class Mail_client():
    def __init__(self, user = str(), passwd = str(), max_msg = 10):

        if user != str():
            self.username = user
        else:
            self.username = raw_input("username: \n")

        if passwd != str():
            self.password = passwd
        else:
            self.password = raw_input("password: \n")

        
        self.msn = Messenger()
        self.msn.username = self.username
        self.msn.password = self.password
        
        self.t_l = Thread_launcher

        self.msn.silent = True
        
        self.t_sender = self.t_l(self.send_loop, None)
        self.t_receiver = self.t_l(self.receive_loop, None)
        
        self.received = list()
        self.sent = list()
        
        self.silent = True
        
        self.max_msg = max_msg
        

        self.tags = ["from: ",
                     "to: ",
                     "subject: ",
                     "body:",
                     "attachements:"]

    def Unformat_str(self, Formatted = str(), tags = list()):
        tokens = Formatted
        
        if tags == list():
            tags = self.tags
            
        okazaki = dict()

        tag_position = list()
        for tag in tags:
            
            start = tokens.find(tag)
            
            if start != -1:
                end = start + len(tag)
            else:
                continue

            tag_position.append([start, end])

        i = 0
        for pos in tag_position:
            if i < len(tag_position) -1:
                okazaki[tags[i]] = tokens[pos[1]: tag_position[i+1][0]]
            else:
                okazaki[tags[i]] = tokens[pos[1]:]

            i += 1

        return okazaki
                
    def send_loop(self):

        user = self.username
        passwd = self.password

        while True:
            try:

                #raw_input()
                #for msg in msgs:
##                for tag in self.tags:
##                    if tag not in msg:
##                        msg[tag] = str()
                to = raw_input("to: \n")
                sub = raw_input("subject: \n")
                body = raw_input("body: ")
                attachs = list()
                while True:
                    attach = raw_input("attach [to leave: blank/None/space char]: \n")
                    if attach == str() or attach == " " or attach == "None":
                        break
                    
                    else:
                        attachs.append(attach)
                
                self.msn.send(user,
                              passwd,

                              mail_to = to,
                              subject = sub,
                              text = body,
                              attach = attachs)
                              
##                              msg["to: "],
##                              msg["subject: "],
##                              msg["body:"],
##                              msg["attachements:"])

            except KeyboardInterrupt:
                break

            except:
                raise

    def receive_loop(self, pause = int()):
        print "receiving started"
        while True:
            try:
                received = self.msn.receiver()
                for msg in received:
                    print msg.Formatted
                pass
            except KeyboardInterrupt:
                break

            except:
                
                error = "error: " + str(sys.exc_info())
                #print type(sys.exc_info())
                print error
                
                time.sleep(pause)
                continue
                #raise

    def run(self):
        pass

if __name__ == "__main__":
    argvs = sys.argv

    if len(argvs) != 1:
        
        try:
            if argvs.count("-u"):
                user = argvs[argvs.index("-u") +1]
            else:
                user = str()
                
            if argvs.count("-p"):
                passwd = argvs[argvs.index("-p") +1]
            else:
                passwd = str()

            if argvs.count("-t"):
                receive_pause = int(argvs[argvs.index("-t") +1])
            else:
                receive_pause = 5
            
        except:
            raise
        
        if argvs[1] == "receive":
            m = Mail_client(user, passwd)
            m.receive_loop(pause = receive_pause)
        
        elif argvs[1] == "send":
            m = Mail_client(user, passwd)
            m.send_loop()
        
        else:
            #use ncli instead
            m = Mail_client(user, passwd)
            
            m.t_receiver.start()
            m.t_sender.start()
            m.t_receiver.join()
            m.t_sender.join()
            
            #Both
            

    else:

        print ("""
_________________________________________________________________________

program: %s
directory: %s
credits: %s
coded by: %s
license: %s
usage: %s
_________________________________________________________________________

""" % (
        os.path.basename(__file__),
        os.path.dirname(__file__),
        __init__.__credits__,
        __init__.__author__,
        __init__.__license__,
        __usage__
        ))
        
        
        
#msn.remove not used, maybe it can be a needing code
