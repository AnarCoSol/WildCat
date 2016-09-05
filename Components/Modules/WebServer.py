def WebServer(args = [8888, "/"]):
    port = args[0]
    directory = args[1]
    import BaseHTTPServer
    import SimpleHTTPServer
    import os
    server_address = ("", port)
    PUBLIC_RESOURCE_PREFIX = '/'
    PUBLIC_DIRECTORY = directory

    os.chdir(PUBLIC_DIRECTORY)

    class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def translate_path(self, path):
            if self.path.startswith(PUBLIC_RESOURCE_PREFIX):
                if self.path == PUBLIC_RESOURCE_PREFIX or self.path == PUBLIC_RESOURCE_PREFIX + '/':
                    return PUBLIC_DIRECTORY + ''
                else:
                    return PUBLIC_DIRECTORY + path[len(PUBLIC_RESOURCE_PREFIX):]
            else:
                return SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self, path)

    httpd = BaseHTTPServer.HTTPServer(server_address, MyRequestHandler)
    print "serving at localhost:" + str(server_address[1])
    httpd.serve_forever()

def CheckPort(url = "localhost", port = 80):
    import socket
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((url,port))
    if result == 0:
       return True
    else:
       return False

def PortChecker(url, port):
    if CheckPort(url, port):
        port +=1
        port = PortChecker(url, port)

    else:
        return port
    return port

def SimpleWebServer(args = [8888, "/"]):
    try:
        port = args[0]
        directory = args[1]

        import socket
        import SimpleHTTPServer
        import SocketServer
        import os
        import sys
        
        if not os.path.isdir(directory):
            directory = os.path.dirname(directory)
            
        os.chdir(directory)

        class MyTCPServer(SocketServer.TCPServer):
            def server_bind(self):
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.socket.bind(self.server_address)

        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = MyTCPServer(("", int(port)), Handler)

        print "serving at port:", str(port)

        httpd.serve_forever()

    except KeyboardInterrupt:
        print "stopping server.."
        exit()

    except:#need better exception handlers as i.e. except porterror:
        raise
        e = str(sys.exc_info())
        if e[:len("(<class 'socket.error'>, error(98,")] == "(<class 'socket.error'>, error(98,":
            port += 1
            print "trying at port: " + str(port)
            SimpleWebServer(args = [port, directory])

if __name__ == "__main__":
    SimpleWebServer([8888,raw_input("dir to serve: ")])
