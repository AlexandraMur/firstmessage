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


def server(dispatcher, dict):
    writable = lambda x: False

    def __init__(self, host=None,port=31337):
        dispatcher.__init__(self)

        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(0xA)
        self.get_message()


    def handle_accept(self):
        sock, (host,port) = self.accept()



def main():
    try:
        asyncore.loop()
    except:
        sys.exit(0)


if __name__ == '__main__':
    main()