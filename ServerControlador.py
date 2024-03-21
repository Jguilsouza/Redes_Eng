import socket


saida_values = []
SaidaAnt = 0

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    global SaidaAnt

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + data)
        Retornosensor = plantadeNivel(float(data))
        conn.send(bytes(str(Retornosensor), 'utf-8'))

    conn.close()

def plantadeNivel(AcaodeControle):
    global SaidaAnt
    Saida = (0.9048* SaidaAnt) + 0.0956 * AcaodeControle
    SaidaAnt = Saida
    return Saida

if __name__ == '__main__':
    server_program()
