"""Generate random license plate images."""
import cv2

import pixels
import tokens
from license_plate import LPImageGenerator, Pattern

if __name__ == "__main__":
    # What the license would be like?
    target = [
        tokens.PROVINCES,
        tokens.ALPHABETS,
        [tokens.ALPHABETS, tokens.DIGITS],
        [tokens.ALPHABETS, tokens.DIGITS],
        [tokens.ALPHABETS, tokens.DIGITS],
        [tokens.ALPHABETS, tokens.DIGITS],
        [tokens.ALPHABETS, tokens.DIGITS]
    ]
    pattern_blue = Pattern(target)

    # The generator.
    generator = LPImageGenerator(pattern_blue)

    # Where is the background imagefile?
    background = cv2.imread('assets/background/blue/140.png')

    # Where are the token image files?
    token_dir = 'assets/tokens/condensed-0'

    # Generate a license.
    license, license_str = generator.random_generate()
    print(license_str)

    # Overlay the mask.
    # result = pixels.overlay(background, mask, (0, 0), (255, 255, 255))

    # Show the results.
    # cv2.imshow('result', result.astype(np.uint8))
    # cv2.waitKey(0)
