# !/usr/bin/python3
#pkg opencv-python, pillow, numpy, PyUserInput

import cv2
import numpy as np
from PIL import ImageGrab
import time

screenX = 713
screenY = 355
screenX1 = 1400
screenY2 = 850
screenshot = ImageGrab.grab((713, 355, 1400, 850))
screenImage = 'screenshot.jpg'
screenshot.save(screenImage)

template=cv2.imread('1.png',1)
backIMG=cv2.imread(screenImage,1)
(WHeight, WWidth, n)=template.shape

result=cv2.matchTemplate(backIMG, template, cv2.TM_CCOEFF)
(_, _, minimumLocation, maximumLocation) = cv2.minMaxLoc(result)
topLeft = maximumLocation
#得到 obj 坐标
objX = topLeft[0] + screenX
objY = topLeft[1] + screenY
print('找到图片对象坐标为：',topLeft[0] + screenX, topLeft[1] + screenY)

#鼠键操作
from pymouse import PyMouse
from pykeyboard import PyKeyboard

mouse = PyMouse()
key = PyKeyboard()
x_dim, y_dim = mouse.screen_size()
print(x_dim, y_dim)
mouse.click(objX,objY,2)
