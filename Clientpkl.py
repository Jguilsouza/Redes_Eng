import socket
import cv2
import pickle
import struct


def client():
    host = socket.gethostname() # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)  # instantiateq
    client_socket.connect((host, port))  # connect to the server
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        try:
                  
            data2 = open('./1234.pkl','rb')
            frame = pickle.load(data2)
            print("a")
            print("Frame",frame)
            data2.close()

        
            cv2.imshow("RECEIVING VIDEO", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

        except Exception as i:
            print(i)
            pass
    client_socket.close()


if __name__ == '__main__':
    client()
