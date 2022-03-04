"""Generate random license plate images."""
import cv2

import patterns
from license_plate import LPImageGenerator

if __name__ == "__main__":
    # What the license would be like?
    pattern_blue = patterns.BLUE
    generator = LPImageGenerator(pattern_blue)

    # Generate some license plates.
    for _ in range(5):
        result = generator.random_generate()

        # Show the results.
        cv2.imshow('result', result)
        cv2.waitKey(0)
