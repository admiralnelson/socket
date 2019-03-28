import socket
import time

ADDRESS = "127.0.0.1"
PORT = 1443

def connect():
    soket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    strToSend = ""
    while(True):
        input(strToSend)
        soket.sendto(strToSend, (ADDRESS, PORT))
        start = time.time()
        try:
            data, server = soket.recvfrom(2048)
            end = time.time()
            latency = end - start
            print(data, " ", latency, "ms")
        except socket.timeout:
            print("REQUEST time out")

connect()