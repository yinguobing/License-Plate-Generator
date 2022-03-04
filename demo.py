"""Generate random license plate images."""
import cv2
import numpy as np

import pixels
from license_plate import generate, TOKENS

if __name__ == "__main__":
    # Where is the background imagefile?
    backgroud = cv2.imread('assets/blue_140.png')

    # Where is the mask image file?
    mask_img = cv2.imread('assets/green_粤.jpg')
    mask = pixels.img_to_mask(mask_img, threshold=128, reverse=True)*255

    # Generate a license.
    license = generate(size=7, tokens=TOKENS)
    print(license)

    # Overlay the mask.
    result = pixels.overlay(backgroud, mask, (0, 0), (255, 255, 255))

    # Show the results.
    cv2.imshow('result', result.astype(np.uint8))
    cv2.waitKey(0)
