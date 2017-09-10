# !/usr/bin/python3
#pkg opencv-python, matplotlib

import cv2
import numpy as np
import matplotlib.pyplot as plt

mrW=cv2.imread('5.png',1)
backIMG=cv2.imread('0.png',1)
(WHeight, WWidth, n)=mrW.shape
result=cv2.matchTemplate(backIMG, mrW, cv2.TM_CCOEFF)
print(result)
(asome, bsome, minimumLocation, maximumLocation) = cv2.minMaxLoc(result)
topLeft = maximumLocation
print(asome, bsome)
print(topLeft[0],topLeft[1])
bottomRight = ((topLeft[0] + WWidth), (topLeft[1] + WHeight))
roi = backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]]
mask = np.zeros(backIMG.shape, dtype="uint8")
backIMG = cv2.addWeighted(backIMG, 0.25, mask, 0.75, 0)
backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]] = roi
plt.figure(0)
plt.imshow(backIMG)
plt.show()