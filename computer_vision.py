import cv2 as cv
import numpy as np

# OpenCV functions
def rescaleFrame(frame, scale):
    """Rescale the frame of an image or video"""

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def translate(img, x, y):
    """Translate the image by x and y"""

    translation = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, translation, dimensions)