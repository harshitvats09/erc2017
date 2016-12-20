import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([7,45,10])
    upper_skin = np.array([28,200,140])

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    median = cv2.medianBlur(res, 15)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('median', median)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
