"""Generate random license plate images."""
import cv2

from core.license_plate import LPImageGenerator
from patterns.china import BLUE

if __name__ == "__main__":
    # What the license would be like?
    generator = LPImageGenerator(BLUE)

    # Generate some license plates.
    for _ in range(100):
        result = generator.random_generate()

        # Show the results.
        cv2.imshow('result', result)
        cv2.waitKey(100)
