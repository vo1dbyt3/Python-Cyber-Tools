import socket

port = 6767
addr = "127.0.0.1"
connecting = True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((addr, port))

server.listen()
print("listening...")

client, address = server.accept()
print("Connected:", address)

while connecting:
    messageFromClient = client.recv(1024)
    decodedmsg = messageFromClient.decode()

    if decodedmsg == "exit":
        print("Connection lost")
        connecting = False
    else:
        print("Client:", decodedmsg)

client.close()
server.close()