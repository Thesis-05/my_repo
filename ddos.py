import socket
from time import sleep

def send_packet(ip, port):
 for i in range(100):
    try:
        # Create a TCP connection to the target server
        s = socket.socket()
        s.connect((ip, port))

    # Send a SYN packet to initiate a connection
        s.sendall(b"SYN")
        s.close()
        print("Sent SYN to port %d" % (port + i))

    # Wait for the response from the target server
        sleep(1)
    except socket.error:
        print("Unable to connect to %s:%d" % (ip, port))
        return True
    else:
        return False
    

send_packet("192.168.31.55",22)

# import socket
# from time import sleep

# def send_packet(ip, port):
#     for i in range(100):
#         try:
#             # Create a TCP connection to the target server
#             s = socket.socket()
#             s.settimeout(1)  # Set a timeout for the connection attempt
#             s.connect((ip, port + i))

#             # Send a SYN packet to initiate a connection
#             s.sendall(b"SYN")

#             # Wait for the response from the target server
#             response = s.recv(1024)

#             if response == b"SYN-ACK":
#                 print("Received SYN-ACK from port %d" % (port + i))

#             # Close the connection
#             s.close()

#         except socket.error as e:
#             print("Unable to connect to %s:%d - %s" % (ip, port + i, e))

#     return True

# # Example usage
# ip_address = "127.0.0.53"
# target_port = 53
# send_packet(ip_address, target_port)




