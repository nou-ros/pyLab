## Networking

# IP Address 
A unique string of numbers separated by full stops that identifies each computer using the internet protocol to communicate over a network. 192.168.0.104.

ping google.com - will show the ip address of google. We can reach out to a website using its ip address.

public_ip: Ip address provided by the ISP. with which we can communicate with the outside world. 

private_ip: Ip address provided by say dhcp with which we can communicate internally but not with the outside. 

ipconfig - cmd
ifconfig - linux/unix

Static ip address remains same. 
Dynamic ip addresses changes frequently.

# Ports: 
We can think of ports as exact house or apartment numbers. So IP addresses represent the city and street name and the port number represents the exact house number we live in.

So when a computer tries to connect or communicate with another computer it needs both the IP address and the Port.

So whenever we are making an application that connects one computer to another we have to make sure that we are not using the common ports. 

List of some important modules in python network/internet programming

| Protocol  |     Function      |  Port No. |         Python module      |
|-----------|:-----------------:|----------:|:--------------------------:|
|   HTTP    |     Web pages     |    80     | httplib, urllib, xmlrpclib |
|   NNTP    |    Usenet news    |    119    |           nntplib          |
|   FTP     |   File Transfer   |    20     |       ftplib, urllib       |
|   SMTP    |   Sending email   |    25     |           smtplib          |
|   POP3    |   Fetching email  |    110    |           poplib           |
|   IMAP4   |   Fetching email  |    143    |           imaplib          |
|   Telnet  |   Command lines   |    23     |           telnetlib        |
|   Gopher  | Document Transfers|    70     |       gopherlib, urlib     |



to find common ports: 
https://www.webopedia.com/reference/portnumbers/

# Socket
A network socket is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network. An endpoint is a combination of an IP address and a port number. Common socket commands in python:
socket.socket() - If we want to communicate from one pc to another pc we have to create a socket with the following command. 
s.bind(host, port) - Binding the ip address and the port number with the socket. 
s.send() - sending message to another pc. 
s.listen() - listening to the message of the sending pc. 
s.recv() - receiving the message and decoding it. 
s.close() - close the socket connection.

server: server file will be in a server.
client: client file will be in a victim's pc.
