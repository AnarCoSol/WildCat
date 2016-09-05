import sqlite3 as lite
import sys
import os

from System_interpreter import System_interpreter
from Text_manipulator import Text_manipulator

class SQLite_agent():
    def __init__(self, db_name = str()):
        
        self.silent = False
        
        s = System_interpreter()
        self.tm = Text_manipulator()
        self.cmd = s.command

        self.db = db_name
            
    def auto_new_db(self, db = str()):
        self.cmd("sqlite3 " + db +" -cmd .tables .exit")
        return db
    
    def man_ol_if(self, sql_line = str()):
        try:
            if self.silent:
                print "manual one line interface"
                print sql_line    
            try:
                self.con = lite.connect(self.db)
            except:
                self.con = lite.connect(self.auto_new_db(self.db))

            with self.con:
                self.cur = self.con.cursor()
                #ctrl-D exception
                self.cur.execute(sql_line)
                data = self.cur.fetchall()
                
            return data
        except:
            raise
            
    def man_ml_if(self, sql_script = str()):
        try:
            if not self.silent:
                print "manual multi line interface"
                
            if sql_script[-4:] == ".txt":
                try:
                    sql_script = self.tm.Read(sql_script)
                except:
                    raise

            try:
                self.cur.executescript(sql_script)
                self.con.commit()
                data = self.cur.fetchall()

                return data
                
            except lite.Error, e:

                if self.con:
                    self.con.rollback()

                return "Error %s " % e.args[0]
                sys.exit(1)
        except:
            raise

    def auto_exit(self):
        if self.con:
            self.con.close()
            


if __name__ == "__main__":
    arg = sys.argv
    s_a = SQLite_agent("test.db")
    while True:
        try:
            s_a.man_ol_if(raw_input("sqlite> "))
        except:
            print "error"
