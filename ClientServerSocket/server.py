import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 15555))
sock.listen(1)
sock.settimeout(120)


while True:
    print('\nWaiting data...')
    conn, addr = sock.accept()
    print('Connect from:{}'.format(addr))
    conn.settimeout(60)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        sdt = (data.decode('utf8'))
        print('\nData from client :', sdt)
        conn.send(bytes(' '.join(sorted(sdt.split(), key=float)), 'utf8'))
    conn.close()


