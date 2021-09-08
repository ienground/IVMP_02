import sys
import cv2  # opencv-python
import numpy as np
import matplotlib.pyplot as plt

print("Python version: ", sys.version)
print("Opencv version: ", cv2.__version__)
print("numpy version: ", np.__version__)
print(__file__)

fileName = "pic.png"
im = cv2.imread(fileName)

# plt.imshow(im)
# plt.show()

cv2.imshow("mywindow", im)
ch = cv2.waitKey()
