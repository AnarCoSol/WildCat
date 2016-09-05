import webbrowser as wb

import webview

import sys

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) != 1:
        if argvs[1] == "-u":
            if len(argvs) !=3:
                if argvs[3] == "-w":
                    print "webview opening: " + argvs[2]
                    
                    webview.create_window(__file__, argvs[2])
                    
            else:
                
                try:
                    print "web browser opening: " + argvs[2]
                    wb.open(argvs[2])
                except:
                    pass
    else:
        print "usage: python web_browser.py -u [url] -w"
    
