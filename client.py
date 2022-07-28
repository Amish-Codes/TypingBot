import socket

# send message
while True:
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    s.connect(('Your IPV4', 9999))
    message = input('> ')
    s.send(message.encode('ascii'))
    if message == 'quit':
        break
    s.close()