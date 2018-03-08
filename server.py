import socket

HOST = '0.0.0.0' # means server will bind to any IP
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server socket.setsockopt(sockez.SOL_SOCKET, socket.SO_REUSFADDR, 1)
server_socket.bind((HOST, PORT))
server_socket,listen(5) # 5 connections max in queue at a time

# see socket documentation to understand how socket.accept works
client_socket, (client_ip, client_port) = server_socket.accept() # accepts incoming connection


while True:

    command = raw_input (">")
    client_socket.send(command)

    if(command == "quit"):
        break

    data = client_socket.recv(1024)
    print(data)

client_socket.close()        