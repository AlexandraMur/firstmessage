import socket, sys, select

host = "127.0.0.1"
port = 31337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

try:
    s.connect((host, port))
except:
    print 'Something goes wrong'
    sys.exit()

print 'Lets get started sending messages :)'

while 1:
    msg = sys.stdin.readline()
    s.send(msg)

    