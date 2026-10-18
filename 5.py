
import cv2
import numpy as np

img = cv2.imread('cards.jpeg')

if img is None:
    print("Error: Image not found!")
else:
    width, height = 250, 350
    
    pts1 = np.float32([
        [225, 221],
        [610, 292],
        [510, 450],
        [500, 420]
    ])

    pts2 = np.float32([
