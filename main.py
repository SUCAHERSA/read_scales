import socket
from read_scales import read_scales

# Configuración del servidor
host = 'localhost'
port = 1111

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Servidor escuchando en {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión desde {addr}")

    # Recibir datos del cliente
    data = client_socket.recv(1024)
    if data:
        print(f"Datos recibidos del cliente: {data.decode('utf-8')}")

        # Enviar respuesta al cliente
        weight = read_scales()
        response = "Datos recibidos correctamente"
        client_socket.sendall(weight.encode('utf-8'))

    client_socket.close()
