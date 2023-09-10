
import socket

HOST = "http://sockettest-sample-network-5555dd2dc0236c96.elb.us-west-2.amazonaws.com"
PORT = 80

def client_program():
    client_socket = socket.socket()  # instantiate
    client_socket.connect((HOST, PORT))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
