import socket

def server_program():
    try:
        host = socket.gethostname()
        port = 80

        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(2)
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("from connected user: " + str(data))
            #data = input(' -> ')
            conn.send(data)  # send data to the client
    except Exception as e:
        print("errror:", e)

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
