import socket, sys, select


def prompt():
    sys.stdout.write('You: ')
    sys.stdout.flush()


host = "127.0.0.1"
port = 31337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

try:
    sock.connect((host, port))
except:
    print 'Something goes wrong'
    sys.exit()

print 'Lets get started sending messages :)'

while 1:
    socket_list = [sys.stdin, sock]
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for s in read_sockets:
        if s == sock:
            data = s.recv(4096)
            if not data:
                print '\nDisconnected'
                sys.exit()
            else:
                sys.stdout.write(data)
                prompt()

        else:
            msg = sys.stdin.readline()
            sock.send(msg)
            prompt()