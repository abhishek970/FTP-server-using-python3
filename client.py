#client.py file
#python version - 3.7.9 (aug 17,2020)
#abhishek970
import socket
import os

HOST = 'localhost'
PORT = 4444
s = socket.socket()
s.connect((HOST, PORT))       # Connecting to server
print('client is online...')
print('Need help?')
while True:
    msg = input(str('CLIENT :')).encode()
    s.send(msg)                  
    r = s.recv(1024).decode()    

    if r == 'dl_ack':
        print('SERVER: File Name?')
        msg_file = input(str('CLIENT :')).encode()
        s.send(msg_file)         
        r = s.recv(1024).decode()
        if r == 'OK':
            msg = str('OK').encode()
            s.send(msg) 
            r_size = int(s.recv(1024).decode())
            s.send(msg) 
                    #file receive
            path_var = str(os.getcwd())+'\\download'+'\\'+msg_file.decode()
            file = open(path_var,'wb')
            file_data = s.recv(r_size+100) 
            file.write(file_data)
            file.close()
            print('SERVER: DOWNLOADED!')
        else:
            pass    
    else:
        print('SERVER: ',r)
        

