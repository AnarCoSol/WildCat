import sys
import os
import multiprocessing

import Modules
from Text_manipulator import Text_manipulator
from Formatter import Formatter
from Importer import Importer

import __init__
slash = "/" #sketchy
__file__ = os.path.dirname(__init__.__file__) + slash +  __file__.split(slash)[-1]

__usage__ = "python " + __file__  + " [start] -i [in file] -o [out_file]"


class Processor():
    def __init__(self,in_file, out_file):
        
        self.tm = Text_manipulator()
        self.f = Formatter()
        self.i = Importer()

        self.tm.silent = True
        
        self.out_file = out_file
        self.in_file = in_file

        self.links = dict()

        self.links["mail_client.py"] = "bash"
        #self.links["bash"] = "mail_client.py"

        self.links["tg_client.py"] = "bash"
        self.links["bash"] = "tg_client.py"

    def simple_spawn(self, f, arg): #simple cause it can be implemented as multicore/multimachine distributed computation technlology using multiprocessing.manager
        try:
            from multiprocessing import Process
            p = Process(target=f, args = (arg,))
            p.start()
        except:
            raise
        
    def inParse(self, raw):
        #print "\n"
        #print "[p] parsing..."
        raw_list = list()
        listified = self.f.listfy(raw,"\n")

        for line in listified:
            meta_data, data = self.f.filter_in(line)

            if meta_data == None:
                if raw_list!= list():
                    raw_list[-1][1] = raw_list[-1][1] + "\n" + data
                else:
                    #print "-databug in tg_client_API at ln 58 in inParse()-"
                    #print data
                    #print type(data)
                    pass

            else:
                raw_list.append([self.metaInParse(meta_data), data])

        return raw_list

    def outParse(self, meta, data):

        return self.f.filter_out(data, meta)#switch?
        

    
            
        
        
    def metaInParse(self, meta): #meta: [i/o] [n] [program_name]
        print #"\n"
        print #"[p] meta-parsing [%s ]" % (str(meta))

        return meta.split(" ")

    def metaOutParse(self, meta):
        
        return self.f.stringfy(meta, " ")

        return [data_type, istance, prog_name]
    def identyParse(self, data):#maybe it can be an API
        pass

    def metaIdentyParse(self,meta):
        data_type, istance, prog_name = meta

        if data_type == "o": return True
        else: return False
    
    def dataParse(self, data, meta):
        #parsing prog_data oriented to op_data oriented
        try:
            data_type, istance, prog_name = meta
            
            Parser = self.i._get(prog_name.replace(".","_") + "_API.py")
            
            return Parser.P2oParser.Parse(data, meta)
            
            
        except:
            raise
        
      
    def linker(self, meta):
        data_type, istance, prog_name = meta

        if data_type == "i":
            data_type = "o"
        else:
            data_type = "i"

        prog_name = self.links[prog_name]

        return data_type, istance, prog_name
    
    def compute(self, raw):
        #bot part:
        #   -[status]> coded but not implemented as compatible script
        #AI part: <- AI stand for artificial intelligence, but can stand for anarchy/ist intelligence
        #   -[status]> not coded and not implemented, suggest: use pybrain neural networks
        
        #
                
        #print "\n"
        #print "[c] computing [%s ]" % (str(raw))
        
        meta = raw[0]
        data = raw[1]
        #if not self.IdentyParse(data) and or self.metaIdentyParse(meta): return
        if not self.metaIdentyParse(meta): return
        
        data = self.dataParse(data, meta)

        
        meta = self.linker(meta) #that does the trick


        data = self.dataParse(data, meta)
        
        data = self.outParse(self.metaOutParse(meta), data)

        self.output(data)
        
        print data

        
    def output(self, data):
        try:
            #print "\n"
            #print "[o] %s" % (str(data))
            self.tm.Write_as_output(self.out_file, data)
        except:
            raise
        
    def server(self):
        print "[!] running..."
        while True:
            try:
                raw = self.tm.Read_as_input(self.in_file)
                #print "\n"
                #print "[i] %s" % (str(raw))
                raw_list = self.inParse(raw)

                for raw in raw_list:
                    
                    self.simple_spawn(self.compute, raw)

            except KeyboardInterrupt:
                print "\n"
                print "[!] server stopping..."
                break

            except:
                raise
        print "[!] server stopped"
        exit()
        
if __name__ == "__main__":
    argvs = sys.argv

    if len(argvs) != 1:

        if argvs[1] == "start":
            if argvs.count("-i"):
                in_f = argvs[argvs.index("-i") + 1]

            if argvs.count("-o"):
                out_f = argvs[argvs.index("-o") + 1]
                
            processor = Processor(in_file = in_f, out_file = out_f)
            processor.server()

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
        
    
    #run asking input in a txt file, spawn computing process and print result to txt file
