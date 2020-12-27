import socket
from Gauss_Random import Gauss_Random

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024).decode().strip().split()
        print(data)

        object = Gauss_Random(int(data[0]), int(data[1]))
        client_sock.sendall(object.get_random_value().encode())
        break

    client_sock.close()