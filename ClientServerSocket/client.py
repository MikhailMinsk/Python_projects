import socket

sock_ = socket.socket()
sock_.connect(('127.0.0.1', 15555))
print('You have a minute to input data or server is closed !')

while True:
    data = input('\nInput data: ')
    if not data:
        break
    sock_.send(data.encode())
    data = sock_.recv(1024)
    if not data:
        break
    print('Data from server: ', data.decode('utf8'))

sock_.close()
