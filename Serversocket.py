import socket
import cv2
import pickle 
import struct
import time

def storeData(data, path): 
    # initializing data to be stored in db 
    db = (data)
    # Its important to use binary mode 
    dbfile = open(path, 'wb')
    # source, destination 
    pickle.dump(db, dbfile)                   
    dbfile.close()

def server(show_video=False):
    # get the hostname
    # host = socket.gethostname()
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)  # get instance

    # Adress of the server
    socket_address = (host, port)

    # Socket Bind
    server_socket.bind(socket_address)

    # Socket Listen
    server_socket.listen(2)
    print("LISTENING AT:", socket_address)

    # Socket Accept
    while True:
        client_socket, addr = server_socket.accept()
        print('GOT CONNECTION FROM:', addr)
        if client_socket:
            vid = cv2.VideoCapture(0)
           

            while (vid.isOpened()):
                _, frame = vid.read()
                
                # Convertes the frame to a serialized object(bytes sequence)
                a = pickle.dumps(frame)
                # Pack the length of the frame and the frame
                message = struct.pack("Q", len(a))+a
                tempo = time.time()
                client_socket.sendall(message)
                print("Socket time", time.time()-tempo)
                
                tempo2 = time.time()
                storeData(frame,'./123.pkl')
                print("Pkl time", time.time()-tempo2)
                if show_video:
                    cv2.imshow('TRANSMITTING VIDEO', frame)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        client_socket.close()


if __name__ == '__main__':
    server()
