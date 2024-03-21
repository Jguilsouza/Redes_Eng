import socket
import cv2
import pickle
import struct


def storeData(data, path): 
    # initializing data to be stored in db 
    db = (data)
    # Its important to use binary mode 
    dbfile = open(path, 'wb')
    # source, destination 
    pickle.dump(db, dbfile)                   
    dbfile.close()

def server(show_video=False):
   
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
                img, frame = vid.read()
                # Convertes the frame to a serialized object(bytes sequence)
                a = pickle.dumps(frame)
                # Pack the length of the frame and the frame
                message = struct.pack("Q", len(a))+a
                #client_socket.sendall(message)

                storeData(frame, './1234.pkl')
                print("Server")

                if show_video:
                    cv2.imshow('TRANSMITTING VIDEO', frame)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('q'):
                        client_socket.close()


if __name__ == '__main__':
    server()
