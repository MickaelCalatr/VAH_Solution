import os
import cv2

def image_save(path, frame):
    name = os.getcwd() + path + frame['Name'] + ".png"
    cv2.imwrite(name, frame['Image'])
