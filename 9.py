import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3)) #Width Identifier
    height = int(cap.get(4)) #Height Identifier


    image = np.zeros(frame.shape, np.uint8)#unsigned integer 8bits
    smaller_Frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_Frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_Frame
    image[:height//2, width//2:] = cv2.rotate(smaller_Frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_Frame


    cv2.imshow('Frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

