#Web GUI Module
import platform
import sys
import webview

class WebGUI():

    def __init__(self, app_type = str()):
        if app_type == str():
            app_type = "ionic"
            
        self.app_type = app_type
        self.WebView = self.PlatformCheck() #return the correct webview for target platform

    def StartGUI(self, url = "/"):
        self.WebView(url)

    def PlatformCheck(self):
        if platform.machine() == "armv7l":
            print "Android armv7l"
            return self.DesktopWebView#self.AndroidWebView

        else:

            print "else"
            return self.DesktopWebView
##            import sys
##
##            if sys.platform == "linux2":
##                print "GNU/Linux X86_64"
##                return self.
##
##            else:
##                print sys.platform
                


    def IOSWebView(self, url = "/"):
        print "not implemented yet, but it's possible"


    def DesktopWebView(self, url = "/"):

        if self.app_type == "browser":
            print "browser started"
            import webbrowser as wb
            
            wb.open(url)

        else:
            
            print "webview started"
            webview.create_window(__file__, url, resizable=True)


        


