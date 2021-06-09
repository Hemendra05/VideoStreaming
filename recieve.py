import cv2
from npsocket import SocketNumpyArray

#cap = cv2.VideoCapture(0)
sock_receiver = SocketNumpyArray()
sock_receiver.initalize_receiver(9998)

while True:
    frame_recv = sock_receiver.receive_array()

    #ret, photo = cap.read()
    #frame = cv2.resize(photo, (240, 240))
    #frame_recv[240:, 400:] = frame

    # Display
    cv2.imshow('frame', frame_recv)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows(13)
