import cv2 as cv
import numpy as np


def rescale(frame, scale):
    """Rescale the frame by x and y"""

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
