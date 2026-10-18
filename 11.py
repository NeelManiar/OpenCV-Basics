import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) #Width Identifier
    height = int(cap.get(4)) #Height Identifier

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])#Light Blue
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange()

    cv2.imshow('Frame', hsv)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


BGR_color = np.array([[[255,0,0]]])
print(cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV))