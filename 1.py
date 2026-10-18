import cv2

#How to Import an Image
img = cv2.imread('Sam-Banner.png')
cv2.imshow('Output', img)
cv2.waitKey(0)

#How to Import a Video
cap = cv2.VideoCapture('Youtube Intro.mp4')
while True:
    success,img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)#Width
cap.set(4,480 )#Height
cap.set(10, 100)#Brightness