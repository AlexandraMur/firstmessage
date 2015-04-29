import socket

sock = socket.socket()
sock.bind(('',31337))
sock.listen(10)

try:
    while True:
        conn, addr = sock.accept()

finally:
    sock.close()