import socket, select


def broadcast(sock, message):
    for socket in CONNECTION_LIST:
        if socket != sock and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                CONNECTION_LIST.remove(socket)



CONNECTION_LIST = []
RECV_BUFFER = 4096
PORT = 31337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("127.0.0.1", PORT))
sock.listen(10)

CONNECTION_LIST.append(sock)

print "Server started on port " + str(PORT)

while 1:
    read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

    for s in read_sockets:
        if s == sock:
            sockfd, addr = sock.accept()
            CONNECTION_LIST.append(sockfd)
            print "Client (%s, %s) connected" % addr
            broadcast(sockfd, "[%s:%s] entered room\n" % addr)

        else:
            try:
                data = s.recv(RECV_BUFFER)
                if data:
                    broadcast(s, "\r" + '<' + str(s.getpeername()) + '> ' + data)

            except:
                broadcast(s, "Client (%s, %s) is offline" % addr)
                print "Client (%s, %s) is offline" % addr
                s.close()
                CONNECTION_LIST.remove(s)
                continue

sock.close()

