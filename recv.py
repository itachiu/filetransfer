import socket

ip_adress = str(raw_input('Enter the IP address to bind the socket: '))

r = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

r.bind((ip_adress,721))

r.listen(5)

print '[+] Waiting for connection'

connection,adresses = r.accept()

print '[+] Connection is made to '+str(adresses)

recive = connection.recv(4096)

file_name = str(recive)

reciving_file = open(str(file_name),'a')

recive = connection.recv(1)

if ('y' in str(recive) or 'Y' in str(recive)):

    while True:

        recive = connection.recv(4096)

        if 'ENDOFFILE' in str(recive):break

        else:reciving_file.write(str(recive))

else:

    print '[+] transfer is aborted'

r.close()
connection.close()
reciving_file.close()
