import socket

def start_send(mean, val):
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 53210))
    string = f"{mean} {val}"
    client_sock.sendall(string.encode())
    data = client_sock.recv(1024)
    client_sock.close()
    return data
