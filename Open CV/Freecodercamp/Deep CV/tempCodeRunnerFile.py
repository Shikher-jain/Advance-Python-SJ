import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,      Flatten, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers.legacy import     SGD

IMG_SIZE = (80,80)
channels = 1
char_path = r'F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Deep CV/4/simpsons_dataset'
p="F:\SHIKHER-VS\Advance-Python-SJ\Open CV\Freecodercamp\Deep CV\4\simpsons_dataset/abraham_grampa_simpson/pic_0000.jpg"
# Creating a character dictionary, sorting it in descending order

char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path,char)))

# Sort in descending order
char_dict = caer.sort_dict(char_dict, descending=True)
print(char_dict)
