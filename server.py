#server.py file
#python version - 3.7.9 (aug 17,2020)
#abhishek970
import socket  # Import socket module
import os
HOST = 'localhost'   # Get local machine 
PORT = 4444 
s = socket.socket()   # Create a socket object
s.bind(('', PORT))    # Bind to the port
s.listen(2)           # Now wait for client connection.
print (s)
print ('FTP Server is ready....!!!')
print('....Please connect an online CLIENT....')
print('Waiting for connection....')
ops = ['help','file','download']
conn,addr=s.accept()
print ('connect by',addr,conn) # Establish connection with client.
while True:
    #communication...
    r = conn.recv(1024).decode()
    print('CLIENT :',r)
    if r in ops:
        if r == 'help':
            msg = str(ops).encode()
            conn.send(msg)
        elif r == 'file':
            top = str(os.getcwd())+'\\store'
            file_name = ''
            for root, dirs, files in os.walk(top):
                file_name = str(files).encode()
                conn.send(file_name)
        elif r == 'download':  #download ops
            buffer = 0 #buffer size variable
            msg = str('dl_ack').encode() #download ack
            conn.send(msg)               
            r = conn.recv(1024).decode() 
            path_var = str(os.getcwd())+'\\store'+'\\'+r
            print(path_var)
            if os.path.exists(path_var):
                msg = str('OK').encode()
                conn.send(msg)       
                r = conn.recv(1024).decode()
                size = os.path.getsize(path_var)
                msg = str(size).encode()
                conn.send(msg)   
                r = conn.recv(1024).decode() 
                #file sending...
                file = open(path_var,'rb')
                file_data = file.read(size)
                conn.send(file_data) 
            else:
                msg = "FILE DOES NOT EXIST".encode()
                conn.send(msg)
       

    else:
        conn.send(str('INVALID COMMAND').encode())

