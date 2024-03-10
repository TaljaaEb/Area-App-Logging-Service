from socket import *
import sys, time
from datetime import datetime
import socket
host = ''
max_port = 8901
min_port = 8899 #80

def scan_host(host, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)

        code = s.connect_ex((host,port))

        if code == 0:
            r_code = code
        s.close()
    except Exception as e:
        print(f"{e}")

    return r_code

def c(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0

try:
    host = input(f"[*] Enter Target Host Address: ")
except KeyboardInterrupt:
    print(f"\n\n[*] User Requested An Interrupt.")
    print(f"[*] Stop.")
    sys.exit(1)

if host == "":
    hostip = socket.gethostbyname(socket.gethostname())
    host = socket.gethostname()
    print(f"\n[*] Host: %s IP: %s" % (host, hostip))
    print(f"[*] Scanning Started At %s...\n" % (time.strftime("%H:%M:%S")))
    start_time = datetime.now()

    for p in range(min_port, max_port):
        for i in range(0,255):
            x = hostip
            res = c(x[:-3]+str(i), p)
            if res:
                print("Device found at: ", x[:-3]+str(i) + ":"+str(p))

if host != "":
    hostip = gethostbyname(host)
    print(f"\n[*] Host: %s IP: %s" % (host, hostip))
    print(f"[*] Scanning Started At %s...\n" % (time.strftime("%H:%M:%S")))
    start_time = datetime.now()

    for p in range(min_port, max_port):
        for i in range(0,255):
            x = hostip
            res = c(x[:-3]+str(i), p)
            if res:
                print("Device found at: ", x[:-3]+str(i) + ":"+str(p))

        
stop_time = datetime.now()
total_time_duration = stop_time - start_time
print(f"\[*] Scanning Finised At %s..." % (time.strftime("%H:%M:%S")))
print(f"\[*] Scanning Duration %s..." % (total_time_duration))
print(f"\[*] Have a nice day !|! ...")
      


    
    

    
    
