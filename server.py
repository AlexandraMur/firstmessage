import socket

def main():
    RECV_BUFFER = 4096
    PORT = 31337

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", PORT))
    sock.listen(10)

    print "Server server started on port " + str(PORT)

    while True:
        try:
            data = sock.recv(RECV_BUFFER)
        except:
            sock.close()
            continue

    sock.close()


if __name__ == "__main__":
    main()