import cv2
from npsocket import SocketNumpyArray

cap = cv2.VideoCapture(0)
sock_sender = SocketNumpyArray()

sock_sender.initialize_sender('localhost', 9998)

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, (620, 480))
    sock_sender.send_numpy_array(frame)
