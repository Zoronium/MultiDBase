import socket
import io

HOST, PORT = "localhost", 12345
data = " "

def com_li(object):
    eval(object)

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
    
        data = input('Enter msg to send : ')
        sock.sendall(bytes(data , "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        print("Received: {}".format(received))
        
        if input('again ?') == 'exit': break 
        else: continue
