# import socket programming library
import socket
# import thread module
from _thread import *
import threading

FORMAT = 'utf-8'
HOST = 'localhost'
PORT = 12345

print_lock = threading.Lock()
temp_file = {}

perf_act = {
    'GET':"print('get')" ,  'MGET':"print('mget')",    # multi get
    'SET': "print('set')", 'MSET':"print('mset')" ,    # multi set
    'FLUSH':"print('flush')" ,  # drop database
    "DELETE" :"print('delete')"  # del key value
}
prfix = {  # to add the working here
    '$': 'handler_binary',
    '-': 'handler_Error',
    ':': 'handler_int',
    '*': 'handler_array',
    '%': 'handler_dict',
    '+': 'handler_string', }


def tempfun(object): 
    f = object[0]
    if not object : print( " disconected ")
    list = object.split()
    if list[0] in perf_act:
        eval(perf_act[list[0]])
    else: print(" COMMAND_ERR : command not found ")

# thread function

def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')
            # lock released on exit
            print_lock.release()
            break
        # send back reversed string to client
        c.send(data)
        print(data)
        # tempfun(data.decode(FORMAT))
    # connection closed
    c.close()


def Main():
    host = ""
    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        print("socket binded to port", port)
        # put the socket into listening mode
        sock.listen(5)
        print("socket is listening")

        # a forever loop until client wants to exit
        while True:
            # establish connection with client
            c, addr = sock.accept()
            # lock acquired by client
            print_lock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            # Start a new thread and return its identifier
            start_new_thread(threaded, (c,))


if __name__ == '__main__':
    Main()
