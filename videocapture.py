import numpy as np
import cv2

cap = cv2.VideoCapture('videoviewdemo.mp4')
fourcc = cv2.cv.CV_FOURCC('I', 'Y', 'U', 'V')
#out = cv2.VideoWriter('output.mp4', fourcc, 20, (640,480))
while (cap.isOpened()):
    ret, frame = cap.read()

    if(ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
    else:
        print("end")

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
#out.release()
cv2.destroyAllWindows()

