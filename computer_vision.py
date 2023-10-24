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

def rotate(img, angle, rotation_point=None):
    """Rotate the image by an angle around the rotation point"""

    (height, width) = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width // 2, height // 2)

    rotation_mat = cv.getRotationMatrix2D(rotation_point, angle, 1)
    dimensions = (width, height)

    return cv.warpAffine(img, rotation_mat, dimensions)