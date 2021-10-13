import socket

def echoserver():
    #assign port number
    serve_port = 12000
    #create a socket
    serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind socket to ip and port number
    serve_socket.bind(('127.0.0.1',serve_port))
    #begin listening on socket
    serve_socket.listen(1)

    #loop to accept incoming connection
    while True:
        #store the connection info as a new soket socket and client
        cxt_skt, client = serve_socket.accept()
        print('Connection from: ')
        print(client)
        #rx data
        msg = cxt_skt.recv(1024)
        #process recieved data (here an uppercase)
        msg = msg.upper()
        #send the msg back
        cxt_skt.send(msg)
        print('sending... ' + msg.decode())
        #close the socket
        cxt_skt.close()
        print('connection has been closed')

echoserver()
