"""
Python snippet to create a printable texture that is mouse optic sensor friendly.
Oishik M | 30 September 2022
https://www.github.com/oishikm
"""

import cv2
import numpy as np

CANVAS_SHAPE = (720, 1280)

canvas = np.zeros(CANVAS_SHAPE)
canvas.fill(255)

i_reset_flag = False
j_reset_flag = False

for i in range(0, CANVAS_SHAPE[0], 2):
    for j in range(0, CANVAS_SHAPE[1], 2):
        if i%4 == 0:
            i_reset_flag = not i_reset_flag
        if j%2 == 0:
            j_reset_flag = not j_reset_flag
        if (i_reset_flag == True) and (j_reset_flag == True):
            canvas[i, j] = 0
            canvas[i+1, j] = 0
            canvas[i, j+1] = 0
            canvas[i+1, j+1] = 0
        
cv2.imwrite('./mousepad-sample.png', canvas)