import socket
# for terminal commands
import sys

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

def socket_accept():
    # accepting the connection which will return a connection object and address([0]-ip, [1]-port)
    conn, address = soc.accept()
    print(f'Connection has been established! Ip: {address[0]} and Port: {str(address[1])}')
    # sending commands to client's pc from server
    send_commands(conn)
    # closing the connection
    conn.close()

def send_commands(conn):
    # for sending infinite amount of commands
    while True:
        # taking command
        command = input()
        # uppon quit command, close the connection and socket
        if command == 'quit':
            conn.close()
            soc.close()
            # exiting the terminal
            sys.exit()
        
        
        if len(str.encode(command)) > 0:
            # sending data to client
            # data are sent in byte format from one computer to another computer
            # str.encode(), encoding input commands into bytes
            conn.send(str.encode(command))
            '''
            reciving the data from the client. As the received data will also be in byte format 
            so we have to change it to string format using the following approach. 
            str(conn.recv(1024), "utf-8")
            conn.recv() - receives the client data.
            1024 - bytes are sent as chunks as there can be huge of amount of bytes. Here chunk size is 1024 bytes.
            utft-8 - encoding type. To convert the bytes in utf-8 format so that it can be converted into string with str. 
            '''
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()

'''
1. Create a socket
2. binding the port and host with the socket and listening for the connection.
3. Establish connection with a client(server must be listening).
4. sending commands to clients from server.
5. Add all the functions in a main function.
'''
