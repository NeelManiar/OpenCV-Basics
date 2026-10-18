import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Source Image, #Start Position, #End Position, #Colour, #Thickness

    img = cv2.line(frame,(0,0), (width, height), (255,0,0), 10)#Blue
    img = cv2.line(img,(0,height), (width, 0), (0, 255, 0), 10)#Green
    
    #Source Image, Center Position, Radius, Colour, Line Thickness(-1 to fill)
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), -1)

    img = cv2.circle(img, (500,500), 200, (0,0,255), -1)

    #Font Selection
    font = cv2.FONT_HERSHEY_SIMPLEX
    #Source, Text, Bottom Left Hand Corner, font, font scale colour, line thickness, line type
    img = cv2.putText(img, 'Speed Limit: 40mph', (300,height-200), font,2,(20,250,245), 5, cv2.LINE_AA)


    cv2.imshow('Frame', img)
  
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()