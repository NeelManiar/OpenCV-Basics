import cv2

img = cv2.imread('Sam-Banner.png')

print(img.shape)

imgResize = cv2.resize(img, (500, 500))#Width, Height
print(imgResize.shape)

imgCropped = img[0:200, 200:500]#Height, Width

cv2.imshow('Image', img)
cv2.imshow('Image Resize', imgResize)
cv2.imshow('Image Cropped', imgCropped)
cv2.waitKey(0)