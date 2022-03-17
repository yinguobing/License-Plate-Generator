"""Generate random license plate images."""
import cv2

from core.license_plate import LPImageGenerator
from patterns.china import (BLUE, CONSULATE, DRIVING_SCHOOL, EMBASSY, GREEN_A,
                            GREEN_B, HONGKONG, MACAO, WHITE, YELLOW)

if __name__ == "__main__":
    # What the license would be like?
    generator = LPImageGenerator(CONSULATE)

    # Generate some license plates.
    for _ in range(100):
        image, tokens = generator.random_generate()

        # Show the results.
        print(tokens)
        cv2.imshow('result', image)
        if cv2.waitKey(100) == 27:
            break
