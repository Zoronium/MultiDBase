# import socket programming library
import socket
# import thread module
from _thread import *
import threading

FORMAT = 'utf-8'
HOST = 'localhost'
PORT = 12345
temp_file = {}

print_lock = threading.Lock()
check = False


class EXecut(object):
    def get(key):
        return temp_file[key]

    def mget(list):
        for i in list:
            return temp_file[i]

        list.strip('][').split(', ')

    def set(key, value):
        temp_file[key] = value
        return temp_file

    def mset(list):
        for key, value in list:
            temp_file[key] = value
            return temp_file

    def delete(key):
        del temp_file[key]
        return temp_file

    def flush(*args):
        temp_file = {}
        return temp_file


perf_act = {
    'GET': EXecut.get,   'MGET': EXecut.mget,    # multi get
    'SET': EXecut.set, 'MSET': EXecut.mset,    # multi set
    'FLUSH': EXecut.flush,  # drop database
    'DELETE': EXecut.delete  # del key value
}
prfix = {  # to add the working here
    '$': 'handler_binary',
    '-': 'handler_Error',
    ':': 'handler_int',
    '*': 'handler_array',
    '%': 'handler_dict',
    '+': 'handler_string', }


def check_handler(object):
    if not object:
        print(" disconected ")
    list = object.split()
    #print('\n')
    if list[0] in perf_act:
        _execute = perf_act[list[0]]
        if list[0] in ['GET', 'MGET' , 'DELETE']:
            return _execute(list[1]) # AKA the temp file 
        else:
            return _execute(list[1], list[2]) # AKA the temp file 
    else:
        print(" COMMAND_ERR : command not found ")
    
# thread function


def threaded(connecection):
    while True:
        # data received from client
        data = connecection.recv(1024)
        if not data:
            print('Bye')
            # lock released on exit
            print_lock.release()
            break

        print (check_handler(str(data.decode(FORMAT))))
        # send back reversed string to client
        connecection.send(b" data received from client")
        #print(data , "dis")

    # connection closed
    connecection.close()


def Main():
    host , port  = HOST , PORT
    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        print("socket binded to port", port)
        # put the socket into listening mode
        sock.listen(5)
        print("socket is listening")

        # a forever loop until client wants to exit
        while True:
            # establish connection with client
            connecection, addr = sock.accept()
            # lock acquired by client
            print_lock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            # Start a new thread and return its identifier
            start_new_thread(threaded, (connecection,))


if __name__ == '__main__':
    Main()
