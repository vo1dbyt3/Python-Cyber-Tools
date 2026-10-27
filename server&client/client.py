import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 6767
addr = "127.0.0.1"
connecting = True

try:
    client.connect((addr, port))

    while connecting:
        messageToServer = input("Enter message: ")
        encodedmsg = messageToServer.encode()
        client.send(encodedmsg)

        if messageToServer == "exit":
            connecting = False

except ConnectionRefusedError:
    print("Connection was refused")

client.close()