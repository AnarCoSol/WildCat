import os
import sys

from Modules.SQL_agent import SQLite_agent
#maybe -arg [argument] it can be sistematized 
if __name__ == "__main__":
    args = sys.argv
    
    if len(args) == 1:
        print ("""usage: python queryman.py [option]
                        options available:
                        -f [db_file_name.db]
                        -oif " [one line query] "
                        -mif [multi line query as file.txt]

                """)

    else:
        if "-f" in args:
            
            sql_agent = SQLite_agent(args[args.index("-f") + 1])

            if "-oif" in args:
                print sql_agent.man_ol_if(args[args.index("-oif") + 1][1:-1])

            elif "-mif" in args:
                print sql_agent.man_ol_if(args[args.index("-mif") + 1])
                
            else:
                while True:
                    print sql_agent.man_ol_if(raw_input("sqlite> "))
