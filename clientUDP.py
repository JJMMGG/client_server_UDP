import socket
import select
import time

UDP_IP = 'localhost'
IN_PORT = 5005
timeout = 3


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    #time.sleep(0.5)
    data, addr = sock.recvfrom(1024)
    if data:
        print "File name:", data
        file_name = data.strip()

    f = open(file_name, 'wb')

    while True:
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            print "%s Finish!" % file_name
            f.close()
            break
