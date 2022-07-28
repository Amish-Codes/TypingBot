import socket, keyboard

def copyToClipboard():
    with open('text.txt', 'r') as f:
        lines = f.readlines()

    keyboard.wait('CapsLock')
    for line in lines:
        keyboard.write(line, delay=0.04)

    with open('text.txt', 'w') as f:
        f.truncate(0)

serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

print(socket.gethostbyname_ex(socket.gethostname()))
try:
    ipv4_address = socket.gethostbyname_ex(socket.gethostname())[2][1]
except:
    ipv4_address = socket.gethostbyname_ex(socket.gethostname())[2][0]
print(ipv4_address)

# bind over internet
serversocket.bind((ipv4_address, 5809)) #((ipv4_address, Port))
serversocket.listen(5)
c = 0
while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()
    if c == 0:
        print('Got a connection from %s' % str(addr))
        c += 1
    
    message = clientsocket.recv(1024)

    if message.decode('ascii') == 'quit':
        break
  
    if message.decode('ascii') != 'copy':
        with open('text.txt', 'a') as f:
            f.write(message.decode('ascii') + '\n')
        print(message.decode('ascii'))
    else:
        copyToClipboard()