import socket
# for terminal commands
import sys



host = ''
port = 0
soc = ''

# 1. Creating a socket

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


# 2. binding the port and host with the socket and listening for the connection
def bind_socket():
    try: 
        global host
        global port 
        global soc

        print("Binding the port: "+str(port))

        soc.bind((host, port))

        # listening to the client
        soc.listen(5)

    except socket.error as err:
        # when socket binding fails we will retry again...
        print("Socket binding error: " + str(err) + "\n" + "Retrying....")
        bind_socket()

# 3. Establish connection with a client(server must be listening)
def socket_accept():
    # accepting the connection which will return a connection object with address([0]-ip, [1]-port)
    conn, address = soc.accept()
    print(f'Connection has been established! Ip: {address[0]} and Port: {str(address[1])}')
    # sending commands to client's pc
    send_command(conn)
    # closing the connection
    conn.close()