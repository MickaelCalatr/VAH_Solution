import os
import cv2
import numpy as np
import random as rand

from scipy import misc, ndimage
from skimage.transform import PiecewiseAffineTransform, warp

def get_times(arr, index):
    times_arr = arr[index].split('-')
    start = int(times_arr[0])
    end = int(times_arr[1])
    return start, end

def deforms(image):
    ratio = 5
    rows, cols = image.shape[0], image.shape[1]
    src_cols = np.linspace(0, cols, 20)
    src_rows = np.linspace(0, rows, 10)
    src_rows, src_cols = np.meshgrid(src_rows, src_cols)
    src = np.dstack([src_cols.flat, src_rows.flat])[0]

    # add sinusoidal oscillation to row coordinates
    dst_rows = src[:, 1] - np.sin(np.linspace(0, 3 * np.pi, src.shape[0])) * ratio
    dst_cols = src[:, 0]
    dst_rows *= 1.5
    dst_rows -= 1.5 * ratio
    dst = np.vstack([dst_cols, dst_rows]).T

    tform = PiecewiseAffineTransform()
    tform.estimate(src, dst)

    image = warp(image, tform, output_shape=(rows, cols))
    return image

if __name__ == '__main__':
    # cv2.rectangle(frame['Image'], (xmin, ymin), (xmax, ymax), (255,0,0), 2)
    img = cv2.imread('32.png', cv2.IMREAD_COLOR)
    image = deforms(img)
    cv2.imshow("lalala", image)
    cv2.imwrite("second.png", image)
    cv2.waitKey(0)
