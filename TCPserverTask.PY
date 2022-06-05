#Group 11 Section: S20
#Abdelrhman Mohmed Ahmed 20200318
#Mohamed Mahmoud Mohamed 20200474
#Marwan Tamer Galal 20200508

from socket import *
serverPort= 15200
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The Server is Ready')

while True:

 connectionSocket, address = serverSocket.accept()

 sentence = connectionSocket.recv(1024).decode()
 if sentence == "Exit":
     print (sentence)
     print ('Server Will Exit. ')
     connectionSocket.close()
            
 else: 
    print ('Recevid from Client: ',address,' :',sentence)
    connectionSocket.send (sentence.encode())


    
