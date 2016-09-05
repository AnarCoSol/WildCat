import sys
import time
import signal

class Status_bar():
        def __init__(self,
                     comment = str(),
                     b_comment = str(),
                     progress = ["|","/" ,"-","\\"],
                     dots = [".","..","...","...."],
                     i = int(),
                     k = 3
                     ):
                
                self.progress = progress
                self.b_comment = b_comment
                self.comment = comment
                self.dots = dots
                self.k = k
                self.i = i

        def input_timeout(self, prompt = str(), time_out = int(), func = None):

                class AlarmException(Exception):
                        pass

                def alarmHandler(signum, frame):
                        raise AlarmException

                def nonBlockingRawInput(prompt=str(), timeout=int(), func = None):
                        signal.signal(signal.SIGALRM, alarmHandler)
                        signal.alarm(timeout)
                        try:
                                if not func:
                                        text = raw_input(prompt)
                                else:
                                        text = func(prompt)
                                        
                                signal.alarm(0)
                                return text
                        
                        except AlarmException:
                                pass

                        except KeyboardInterrupt:
                                return "KeyboardInterrupt"

                        except EOFError:
                                pass
                    
                        signal.signal(signal.SIGALRM, signal.SIG_IGN)
                        return None

                text = nonBlockingRawInput(prompt, time_out, func)
                
                return text
		
        def rotate(self):
                rotation = "\r" + self.b_comment + "[%s] " % self.progress[self.i] + self.comment + "%s" % self.dots[self.i]
                sys.stdout.write(rotation)
                
                sys.stdout.flush()
                
                if self.i < self.k:
                        self.i += 1
                else:
                        self.i = 0

                return rotation

        def rotate_in(self, wait_time = int()):
                rotation = "\r" + self.b_comment + "[%s] " % self.progress[self.i] + self.comment + "%s" % self.dots[self.i]

                sys.stdout.write(rotation)
                
                sys.stdout.flush()
                
                key_in = self.input_timeout("", int(wait_time))
                if key_in == "KeyboardInterrupt":
                        exit()
                
                
                if self.i < self.k:
                        self.i += 1
                else:
                        self.i = 0

                #return rotation
                
                
        def __test__(self):
                while True:
                        self.b_comment = time.ctime() + " "
                        self.rotate()
                        time.sleep(1)
                
if __name__ == "__main__":
        s = Status_bar("rotating")
        s.__test__()
