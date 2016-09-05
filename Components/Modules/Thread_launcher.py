import threading

class Thread_launcher(threading.Thread):
    def __init__(self,func,arg):
        threading.Thread.__init__(self)
        self.name = str()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(self.arg)
        
    def launch(self):
        self.start()
        self.join()

if __name__ == "__main__":
    import time
    class prova():
        def __init__(self):
            self.a = 2
            self.b = self.f
        def f(self):
            self.c = 3
        def main(self):
            def f1(s):
                s.f()
                s.a += s.c
            def f2(s):
                while True:
                    print "s.a" + str(s.a)
                    time.sleep(3)
                
            t2 = Thread_launcher(f2, self)
            dir(t2)
            t2.start()
            while True:
                t1 = Thread_launcher(f1,self)

                t1.start()
                t1.join()

                time.sleep(2)
                print "while loop"
    p = prova()
    p.main()
            
