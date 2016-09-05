import webbrowser as wb
import sys

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) != 1:
        if argvs[1] == "-u":
            try:
                print "web browser opening: " + argvs[2]
                wb.open(argvs[2])
            except:
                pass
    else:
        print "usage: python web_browser.py -u [url]"
    
