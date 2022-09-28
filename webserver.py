# import socket
from fileinput import filename
from socket import *
from sqlite3 import connect
# create a TCP server
# example http://128.238.251.26:6789/HelloWorld.html uses the port number 6789

serverPort = 6789
# AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP
# create server socket
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("The web server is up on port: " + serverPort)
while True:
    print("Ready to serve ")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connect.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)
        # send one HTTP header line into the socket
        connectionSocket.send("\nHTTP/1.1 200 OK\n\n".encode())
        connectionSocket.close()
    except IOError:
        # 404 msg
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        connectionSocket.close()
serverSocket.close()



