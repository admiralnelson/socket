import socket
import gc

HOST = "localhost"
PORT = 1443
g_socket = None

def init():
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Socket created!")
    except socket.error as msg:
        print("Failed to create socket ", msg[0], " msg ", msg[1] )
        exit(-1)

    try:
        soket.bind((HOST, PORT))
    except socket.error as msg:
        print("bind failed ", msg[0], " msg ", msg[1])
        exit(-1)

    print("socket ok!")
    return soket

def tick():
    while True:
        data = g_socket.recvfrom(2048)
        recievedData = data[0]
        recievedAddr = data[1]

        if(not data):
            break
        reply = "Received data " + str(data)

        g_socket.sendto( str.encode(reply), recievedAddr)
        print("IP addr: ", recievedAddr, " message ", recievedData)

    g_socket.close()

g_socket = init()
tick()