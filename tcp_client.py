import socket

def echoclient(server, port):
    #ID desired port number
    client_port = port
    #create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #ID desired server IP
    server_name = server
    #connect to server IP on port #
    client_socket.connect((server_name,client_port))
    #pull user input for msg

    msg = input('please type your msg: ')
    #send msg encoded as bits
    client_socket.send(msg.encode())
    #if data recieved store as reply
    reply = client_socket.recv(1024)
    #print the reply data decoded from bits to string
    print('server says: ' + reply.decode())

s = '127.0.0.1'
p = 12000
echoclient(s,p)
