import socket
from threading import Thread
import parser
import os

os.environ["SAPNWRFC_HOME"] = "C:\\Users\\{USER}\\nwrfcsdk"

class Proxy2Server(Thread):

    def __init__(self, host, port):
        super(Proxy2Server, self).__init__()
        self.gui = None # gui client socket not known yet
        self.port = port
        self.host = host #
        #self.URL = ""
        def scl():
            from pyrfc import Connection
            ASHOST = '111.111.111.111'
            CLIENT = '100'
            SYSNR = '00'
            USER = 'user'
            PASSWD = 'password'
            conn = Connection(ashost=ASHOST, sysnr=SYSNR, client=CLIENT, user=USER, passwd=PASSWD)
            return conn
        #self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.server.connect((host,port))
        self.server = scl()
       

    #run in thread
    def run(self):
        while True:
            data = self.server.recv(4096)
            print("[{}] <- {}".format(self.port, data[:100]).encode('hex'))
            if data:
                print("[{}] <- {}".format(self.port, data[:100]).encode('hex'))
                try:
                    reload(parser)
                    parser.parse(data, self.port, 'server')
                except Exception as e:
                    print('server[{}]'.format(self.port), e)
                #forward to client
                self.gui.sendall(data)

class Gui2Proxy(Thread):
   
    def __init__(self, host, port):
        super(Gui2Proxy, self).__init__()
        self.server = None # real server socket not known yet
        self.port = port
        self.host = host
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        sock.bind((host, port))
        sock.listen(1)
        # waiting for a connection
        self.gui, addr = sock.accept()

    def run(self):
        while True:
            data = self.gui.recv(4096)
            print("[{}] -> {}".format(self.port, data[:100]).encode('hex'))
            if data:
                print("[{}] -> {}".format(self.port, data[:100]).encode('hex'))
                try:
                    reload(parser)
                    parser.parse(data, self.port, 'client')
                except Exception as e:
                    print('client[{}]'.format(self.port), e)                
                #forward data to host
                self.server.sendall(data)

class Proxy(Thread):

    def __init__(self, from_host, to_host, port):
        super(Proxy, self).__init__()
        self.from_host = from_host
        self.to_host = to_host
        self.port = port

    def run(self):
        while True:
            print("[proxy({})] setting up".format(self.port))
            self.g2p = Gui2Proxy(self.from_host, self.port)
            self.p2s = Proxy2Server(self.to_host, self.port)
            print("[proxy({})] connection established up".format(self.port))
            self.g2p.server = self.p2s.server
            self.p2s.gui = self.g2p.gui

            self.g2p.start()
            self.p2s.start()

           
master_server = Proxy('0.0.0.0', '111.111.111.111', 3200) #sap host
master_server.start()

gui_clients = []
for port in range(3000, 3006):
    _gui_client = Proxy('0.0.0.0', '172.31.204.62', port) #your ip
    _gui_client.start()
    gui_clients.append(_gui_client)

while True:
    try:
        cmd = input('$ ')
        if cmd[:4] == 'quit':
            os._exit(0)
    except Exception as e:
        print(e)

