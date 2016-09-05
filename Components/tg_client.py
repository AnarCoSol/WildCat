import sys
import os

import __init__#or itself as import mail_client.__file__
slash = "/" #sketchy
__file__ = os.path.dirname(__init__.__file__) + slash +  __file__.split(slash)[-1]

__usage__ = "python " + __file__ + " [receiver/sender/Both] -c [telegram-cli path]"

try:
    from pytg import Telegram
    from pytg.utils import coroutine
except:
    raise


class Tg_client():#it can be receive/send media file and audio otf 

    def __init__(self, tg_path = str()):
        if tg_path == str():
            tg_path = os.path.dirname(__file__) + slash + "tg"
        
        self.tg = Telegram(telegram =  tg_path + slash + "bin" + slash + "telegram-cli",
                      pubkey_file = tg_path + slash + "tg_server.pub")

        self.sender = self.tg.sender

        self.receiver = self.tg.receiver
        
    def receive_loop(self):
        @coroutine
        def main_loop(sender, receiver):
            QUIT = False
            try:
                while not QUIT:
                    msg = (yield) # it waits until it got a message, stored now in msg.
                    sender.status_online()
                    if msg.event != "message":
                        continue
                    
                    if msg.own:
                        continue
                    
                    try:
                        
                        print "from:" + str(msg.sender[unicode("username", "utf-8")])
                        print "msg:" + str(msg.text.encode("utf-8"))
                        #print('Full dump: {array}'.format(array=str(msg)))
                        
                    except:
                        continue
         
                    if msg.text == u"quit":
                        receiver.stop()
                        QUIT = True
            except GeneratorExit:
                receiver.stop()
                QUIT = True
            except KeyboardInterrupt:
                receiver.stop()
                QUIT = True
            else:
                pass

        while True:
            try:
                self.receiver.start()
                self.receiver.message(main_loop(self.sender, self.receiver))
                self.receiver.stop()

            except KeyboardInterrupt:
                print "exiting..."
                break

            except:
                try:
                    info = sys.exc_info()
                    print info
                except:
                    continue
            
        
    def send_loop(self):

        while True:
            try:
                
                to = raw_input("to:\n")
                msg = raw_input("msg:")
                
                self.sender.send_msg(unicode(to.replace(" ", ""), "utf-8"),
                                     unicode(msg, "utf-8"))

            except KeyboardInterrupt:
                break

            except:
                try:
                    info = sys.exc_info()
                    print info
                except:
                    continue

if __name__ == "__main__":
    argvs = sys.argv


    if len(argvs) != 1:


        try:
            if argvs.count("-c"):
                cli_path = argvs[argvs.index("-c") +1]
        
        except:
            raise

        t = Tg_client(cli_path)
        
        if argvs[1] == "receiver":
            t.receive_loop()

        elif argvs[1] == "sender":
            t.send_loop()

        else:
            pass

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
