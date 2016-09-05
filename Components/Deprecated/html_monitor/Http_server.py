#!/usr/bin/python

#imports here
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi
import os

from toolbox.Modules.Text_manipulator import Text_manipulator as T_m
from toolbox.Modules.Messenger import Messenger as Msn
import Http_server

class myHandler(BaseHTTPRequestHandler):
        def default(self, x = str()):
                print x
                        
        ("""def executer(self, x = str()):
                if x[0] == "local": #better using a dict instead of list
                        sh_otf = Local_shell() #otf = on the fly
                        tm_otf = T_m()
                        #os.system(x[1])
                        if x[1] == "clear":
                                tm_otf.Write_new("monitor_text.html","<h2>Monitor 0</h2>")
                        else:
                                tm_otf.Write_add("monitor_text.html","<h2>" +
                                                 str(sh_otf.command(x[1])) +
                                                 "</h2>" + "\n")""")
        def trinity(self, x = str()):
                if x[0] == "local": #better using a dict instead of list
                        tm_otf = T_m()
                        tm_otf.Write_add("in.txt", x[1] + "\n")
                        
        def WS (self, x = str()):
                M_otf = Msn()
                user = "pythonshogun"
                passw = "connection..."
                m_to = "pythonprompt@gmail.com"
                sub = "node python /root/Operator/toolbox/dhws_new.py shutdown"
                txt = "none"
                att = "none"
                try:
                        M_otf.send(user, passw, m_to, sub, txt, att)
                        print "email sended"
                except:
                        print "error sending email"

                        
        #Handler for the GET requests
        def do_GET(self, page = str()):
                default_page = "index.html"
                if self.path=="/":
                        self.path = default_page
                if self.path == "/send":
                        if page != str():
                                self.path = page
                        else:
                                self.path = default_page
                                
                if self.path == "/WS":
                        self.path = default_page

                try:
                        #Check the file extension required and
                        #set the right mime type

                        sendReply = False
                        if self.path.endswith(".html"):
                                mimetype='text/html'
                                sendReply = True
                        if self.path.endswith(".jpg"):
                                mimetype='image/jpg'
                                sendReply = True
                        if self.path.endswith(".gif"):
                                mimetype='image/gif'
                                sendReply = True
                        if self.path.endswith(".js"):
                                mimetype='application/javascript'
                                sendReply = True
                        if self.path.endswith(".css"):
                                mimetype='text/css'
                                sendReply = True

                        if sendReply == True:
                                #Open the static file requested and send it
                                f = open(curdir + sep + self.path) 
                                self.send_response(200)
                                self.send_header('Content-type',mimetype)
                                self.end_headers()
                                self.wfile.write(f.read())
                                f.close()
                        return

                except IOError:
                        self.send_error(404,'File Not Found: %s' % self.path)

        #Handler for the POST requests
        def do_POST(self):
                
                form = cgi.FieldStorage(
                        fp=self.rfile, 
                        headers=self.headers,
                        environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                })

                try:
                        env_checked = form["nodes"].value
                except:       
                        env_checked = "local"

                try:
                        form_raw_text = form["input_text"].value
                except:
                        form_raw_text = str()

                page = self.headers['referer']
                        
                submitted = [env_checked, form_raw_text]
                print submitted
                self.trinity(submitted)
                #self.send_response(200)
                #self.end_headers()
                #self.wfile.write("Thanks %s !" % form["your_name"].value
                self.do_GET(page)
                return
                
                if self.path=="/WS":
                        form = cgi.FieldStorage(
                                fp=self.rfile, 
                                headers=self.headers,
                                environ={'REQUEST_METHOD':'POST',
                                 'CONTENT_TYPE':self.headers['Content-Type'],
                        })
                        print form
                        self.WS()
                        #self.send_response(200)
                        #self.end_headers()
                        #self.wfile.write("Thanks %s !" % form["your_name"].value
                        self.do_GET()
                        return
                
def main(def_func = None, port_numb = int()):
        tm_otf = T_m()
        if port_numb == int():
                port_numb = 8000
        
        while True:
                try:
                        #Create a web server and define the handler to manage the
                        #incoming request


                        server = HTTPServer(('', port_numb), myHandler)
                        print 'Started http server on port ' , port_numb
                        
                        #Wait forever for incoming http requests
                        tm_otf.Write_new("port.txt", str(port_numb))
                        server.serve_forever()
                        
                except KeyboardInterrupt:
                        print '^C received, shutting down the web server'
                        tm_otf.Write_new("port.txt", "")
                        server.socket.close()
                        break
                except:
                        port_numb += 1
                        
if __name__ == "__main__":
        def default_function(x = str()):
                print "input: " + str(x)

        tm = T_m()
        script_path = os.path.dirname(Http_server.__file__)

        p_numb = 8000
                
        main(port_numb = p_numb)
