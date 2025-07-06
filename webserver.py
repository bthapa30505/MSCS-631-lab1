#import socket module
import socket
import sys # In order to terminate the program

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 6789))  # Bind to port 6789 on all available interfaces
serverSocket.listen(1)  # Listen for incoming connections, queue up to 1 connection
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Accept incoming connection
    try:
        message = connectionSocket.recv(1024).decode()  # Receive HTTP request
        filename = message.split()[1]
        f = open(filename[1:])  # Open file (remove leading '/')
        outputdata = f.read()  # Read file content
        
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>".encode())
        #Fill in end
        
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 