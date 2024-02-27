import socket, ssl, sys, os

HOST, PORT, CERT, KEY = '0.0.0.0', 8000, 'cert.pem', 'key.pem'

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = s.getsockname()[0]
    s.close()
    return IP

def get_username():
    USER = os.getlogin()
    return USER

def handle(conn):
  #print(conn.recv())
  BSTRING = conn.recv()
  #conn.write(b'HTTP/1.1 200 OK\n\n%s' % conn.getpeername()[0].encode())
  #conn.write(b'%s' % conn.getpeername()[0].encode())
  ASTRING = LOCAL_IP + LOCAL_USER
  conn.write(b'%s' % ASTRING.encode())

def main():
  sock = socket.socket()
  sock.bind((HOST, PORT))
  sock.listen(5)
  context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  context.load_cert_chain(keyfile=KEY, certfile=CERT, password='password')  # 1. key, 2. cert, 3. intermediates
  context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional
  context.set_ciphers('EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')
  while True:
    conn = None
    ssock, addr = sock.accept()
    try:
      conn = context.wrap_socket(ssock, server_side=True)
      handle(conn)
    except ssl.SSLError as e:
      print(e)
    finally:
      if conn:
        conn.close()
if __name__ == '__main__':
    #REMOTE_IP = str(sys.argv[1])
    LOCAL_IP = get_ip()
    LOCAL_USER = get_username()
    main()
