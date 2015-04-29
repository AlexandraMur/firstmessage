import socket
import asyncore
import sys



#sock = socket.socket()
#sock.bind(('',31337))
#sock.listen(10)

#try:
#    while True:
#        conn, addr = sock.accept()
#        print "connected"
#
#       while True:
#            data = conn.recv(1024)
#            if not data:
#                break
#        conn.close()
#finally:
#    sock.close()


def server(dispather, dict):
    writable = lambda x: False

    def __init__(self, host=None,port=31337):
        dispather.__init__(self)

        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(0xA)
        

def main():
    try:
        asyncore.loop()
    except:
        sys.exit(0)


if __name__ == '__main__':
    main()