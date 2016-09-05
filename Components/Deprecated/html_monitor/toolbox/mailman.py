import os
import sys

from Modules.Messenger import Messenger
#use it to send email
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print ("""usage: python mailman.py [options]
                    options available:
                    -m [send/receive]
                    -u [user]
                    -p [passw]
                    -t [to]
                    -s [sub]
                    -b [body]
                    -a [attach1 attach2]
                """)
    elif len(args) >= 14:
        pass
