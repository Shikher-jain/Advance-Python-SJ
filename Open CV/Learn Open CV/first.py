import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

# %matplotlib inline

# Image(filename="F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Learn Open CV/checkerboard_18x18.png")

# Read the image

img = cv2.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Learn Open CV/checkerboard_18x18.png",0)
print(img)
plt.imshow(img, cmap='gray')
plt.show()

