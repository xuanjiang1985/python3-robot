# !/usr/bin/python3
#pkg opencv-python, matplotlib

import cv2
import numpy as np
import matplotlib.pyplot as plt

mrW=cv2.imread('1.png',1)
backIMG=cv2.imread('0.png',1)
plt.figure(0)
plt.imshow(backIMG)
plt.figure(1)
plt.imshow(mrW)
(WHeight, WWidth, n)=mrW.shape
result=cv2.matchTemplate(backIMG, mrW, cv2.TM_CCOEFF)
(_, _, minimumLocation, maximumLocation) = cv2.minMaxLoc(result)
topLeft = maximumLocation
bottomRight = ((topLeft[0] + WWidth), (topLeft[1] + WHeight))
roi = backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]]
mask = np.zeros(backIMG.shape, dtype="uint8")
backIMG = cv2.addWeighted(backIMG, 0.25, mask, 0.75, 0)
backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]] = roi
plt.figure(2)
plt.imshow(backIMG)
plt.show()

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('1.png',0)
# img2 = img.copy()
# template = cv2.imread('0.png',0)
# plt.imshow(template)
# w, h = template.shape[::-1]

# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)

# # Apply template Matching
#     res = cv2.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
 
#     cv2.rectangle(img,top_left, bottom_right, 255, 2)
 
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#     plt.show()
