#Group 11 Section: S20
#Abdelrhman Mohmed Ahmed 20200318
#Mohamed Mahmoud Mohamed 20200474
#Marwan Tamer Galal 20200508


from socket import *
serverIP = '127.0.0.1'
serverPort= 15200
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
sentence = input ('Input Your message: ')
clientSocket.send(sentence.encode())
modifiedMsg = clientSocket.recv(1024)

print ('from server: ', modifiedMsg.decode(),' Lenth: ',len(modifiedMsg.decode()))
clientSocket.close()
