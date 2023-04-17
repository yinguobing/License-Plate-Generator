"""This module provides image pixel manipulation tools."""
import cv2
import numpy as np
import numpy.ma as ma


def img_to_mask(image: np.ndarray, threshold=128, reverse=False):
    """Convert an image into a binary mask."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(gray, dtype=np.int64)
    mask[gray > threshold] = 1

    if reverse:
        mask = 1 - mask

    return mask


def overlay(image: np.ndarray, mask: np.ndarray, location=(0, 0), color=(0, 0, 0)):
    """Cover the target image by a mask with color.

    Args:
        image: target image.
        mask: a binary 2D array.
        origin: the top left location of the mask to put.
        color: a tuple of 3 uint8 numbers, BGR format.
    """
    # What happens if a mask is not in the good shape?
    assert mask.ndim == 2, f"The mask should be a 2D array, but {mask.ndim}D given."

    # What happens if a mask is larger than the target image?
    img_height, img_width, img_channel = image.shape
    mask_height, mask_width = mask.shape
    assert (img_height >= mask_height) and (img_width >= mask_width),\
        f"The mask shape ({mask_width, mask_height}) should be smaller than the target image shape ({img_width, img_height})"

    # Convert the local mask to an global image mask.
    x, y = location
    _mask = np.zeros((img_height, img_width))
    _mask[y:y+mask_height, x:x+mask_width] = mask

    # Overlay the mask now.
    b, g, r = color
    channel_blue = ma.masked_array(image[:, :, 0], mask=_mask).filled(b)
    channel_green = ma.masked_array(image[:, :, 1], mask=_mask).filled(g)
    channel_red = ma.masked_array(image[:, :, 2], mask=_mask).filled(r)

    # Construct a return image.

    if img_channel == 4:
        channel_alpha = image[:, :, 3]
        result = np.stack([channel_blue, channel_green,
                           channel_red, channel_alpha], axis=-1)
    else:
        result = np.stack([channel_blue, channel_green, channel_red], axis=-1)

    return result
