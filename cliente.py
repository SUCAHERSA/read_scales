import socket

# Configuración del cliente
host = 'localhost'
port = 1111


def detener_socket(sock):
    try:
        sock.shutdown(socket.SHUT_RDWR)
    except Exception as e:
        print(f"Error al cerrar el socket: {e}")
    finally:
        sock.close()


# Crear el socket del cliente
def llamada_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Enviar datos al servidor
    message = "Hola, servidor"
    client_socket.sendall(message.encode('utf-8'))

    # Recibir respuesta del servidor
    response = client_socket.recv(1024)
    print(f"{response.decode('utf-8')}")

    client_socket.close()

    #detener_socket(client_socket)


llamada_socket()


#print("El socket ha sido detenido.")