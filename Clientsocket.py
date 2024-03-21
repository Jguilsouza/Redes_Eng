import socket
import cv2
import pickle
import struct


def client():
    host = "44.204.229.231" # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)  # instantiateq
    client_socket.connect((host, port))  # connect to the server
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        try:
            while len(data) < payload_size:
                packet = client_socket.recv(4*1024)  # 4K
                if not packet:
                    break
                data += packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            openpkl = open('./1234.pkl','rb')
            framepkl = pickle.load(openpkl)
            openpkl.close()

            while len(data) < msg_size:
                data += client_socket.recv(4*1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow("RECEIVING VIDEO", framepkl)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
        
        except Exception as i:
            print(i)
            pass
    client_socket.close()


if __name__ == '__main__':
    client()
