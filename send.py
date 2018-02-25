import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

filename = raw_input('enter the filename in this directory with extension: ')

ip_address = str(raw_input('Enter the ip address: '))

sending_file = open(str(filename),'r')

s.connect((ip_address,721))

print '[+] file is being sent'

s.send(str(filename))

conformation = raw_input("enter Y for transfer for yes/no: ")

s.send(str(conformation))

def sending():
    
    for i in sending_file.readlines():
        s.send(i)

    s.send('ENDOFFILE')
    
    return 0

sending()

print '[+] file is sent'

sending_file.close()
s.close()
