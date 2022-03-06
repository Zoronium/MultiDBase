import socket
import io

HOST, PORT = "localhost", 12345
data = " "


def com_li(object):
    eval(object)

def main():
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        while True:

            sock.sendall(bytes(User_process._CLI(), "utf-8"))

            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")

            print("Sent:     {}".format(data))
            print("Received: {}".format(received))

            if input('again ?') == 'exit':
                break
            else:
                continue


class User_process():
    def menu(self):
        print("""
                
        ███╗░░░███╗██╗░░░██╗███╗░░░███╗██████╗░░█████╗░░░░░░░██████╗░███╗░░░███╗
        ████╗░████║██║░░░██║████╗░████║██╔══██╗██╔══██╗░░░░░░██╔══██╗████╗░████║
        ██╔████╔██║██║░░░██║██╔████╔██║██████╦╝██║░░██║█████╗██║░░██║██╔████╔██║
        ██║╚██╔╝██║██║░░░██║██║╚██╔╝██║██╔══██╗██║░░██║╚════╝██║░░██║██║╚██╔╝██║
        ██║░╚═╝░██║╚██████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝░░░░░░██████╔╝██║░╚═╝░██║
        ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░░░░░░░╚═════╝░╚═╝░░░░░╚═╝
        
    Hello , User plz select what you want to do today
        
        1. view DATABASEs
        2. Chose a DB
        3. USe CLI
        4. USe webCLI (* todo Alpha)
        4. Tweek Settings

        """)
        sel_usr = input(">>> ")
    
    def _manage ():
        if True:
            pass
    def _CLI():
        return input(">>> ")

if __name__ == "__main__":
    main()  