import sys
import os
import webbrowser
import openpyxl
from time import sleep


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Served from {os.getpid()}")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/basic", basicRequestHandler)
    ])

    port = [8882,1111,2222,3333]
    for i in range(len(port)):
        webbrowser.open(f'https://web.whatsapp.com/', port[1])
        sleep(30)
        if (sys.argv.__len__() > 1):
            port = sys.argv[1]
        
        app.listen(port[i])
        print(f"Application is ready and listening on port {port[i]}")
    
    tornado.ioloop.IOLoop.current().start()
