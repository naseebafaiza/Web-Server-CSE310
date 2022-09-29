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
print("The web server is up on port: ", serverPort)
while True:
    print("Ready to serve ")
    connectionSocket, addr = serverSocket.accept()
    try:
        # reads incoming http request and stores in message. 
        # For example "GET /index.html HTTP/1.1"
        message = connectionSocket.recv(2048)
        # splits message by space and gets second element "/index.html"
        filename = message.split()[1]
        # tries to open the file, if file isn't found an exception is thrown
        f = open(filename[1:])
        # reads the file content
        outputdata = f.read()
        print(outputdata)
        # send one HTTP header line into the socket
        res = "HTTP/1.1 200 OK\n\n" + outputdata
        # sends data back encoded in binary
        connectionSocket.send(res.encode()) 
        connectionSocket.close()
    except IOError:
        # 404 msg
        connectionSocket.send("HTTP/1.1 404 Not Found\n\n404 Not Found".encode())
        connectionSocket.close()




