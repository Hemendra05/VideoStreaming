import socket
import numpy as np
import cv2


class SocketNumpyArray():
    def __init__(self):
        self.address = ''
        self.port = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.type = None  # server or client

    def initialize_sender(self, address, port):
        """
        :param address: host address of the socket e.g 'localhost' or your ip
        :type address: str
        :param port: port in which the socket should be intialized. e.g 4000
        :type port: int
        :return: None
        :rtype: None
        """


        self.address = address
        self. port = port
        self.socket.connect((self.address, self.port))

    def send_numpy_array(self, np_array):
        """
        :param np_array: Numpy array to send to the listening socket
        :type np_array: ndarray
        :return: None
        :rtype: None
        """
        data = cv2.imencode('.jpg', np_array)[1].tostring()

        # Send message length first
        HEADER_LENGTH = 10
        message_size = f"{len(data):<{HEADER_LENGTH}}".encode('utf-8')

        # Then data
        self.socket.sendall(message_size + data)

    def initalize_receiver(self, port):
        """
        :param port: port to listen
        :type port: int
        :return: numpy array
        :rtype: ndarray
        """
        self.address = ''
        self.port = port
        self.socket.bind((self.address, self.port))
        print('Socket bind complete')
        self.socket.listen(10)
        self.conn, addr = self.socket.accept()
        print('Socket now listening')


    def receive_array(self):

        HEADER_LENGTH = 10

        message_header = self.conn.recv(HEADER_LENGTH)
        message_length = int(message_header.decode('utf-8').strip())

        data = self.conn.recv(message_length)

        # Extract frame
        nparr = np.fromstring(data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return frame
