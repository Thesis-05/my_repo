import socket
import time
from datetime import datetime



target = input("\nEnter the ip: ")

def port_scan(target):
    try: 
        ip = socket.gethostbyname(target)

        print(f"scanning the target {ip}")
        print("\nTime started", datetime.now())

        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("\nport {}: open".format(port))
            sock.close()
            

    except socket.gaierror:
        print("Hostname could not be resolved")

    except socket.error:
        print("could not connect to the server")

    time.sleep(1)
    print("\nThats it bro no more ports are open")
    print("Time finished", datetime.now())
port_scan(target)
