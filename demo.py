"""Generate random license plate images."""
import cv2

from core.grind import Grinder
from core.license_plate import LPImageGenerator
from patterns.china import (BLUE, CONSULATE, DRIVING_SCHOOL, EMBASSY, GREEN_A,
                            GREEN_B, HONGKONG, MACAO, WHITE, YELLOW)

if __name__ == "__main__":
    # What the license would be like?
    generator = LPImageGenerator(BLUE)

    # How to make the license looks real?
    grinder = Grinder()

    # Generate some license plates.
    for _ in range(100):

        # Generate one license plate.
        image, tokens = generator.random_generate()

        # Grind it!
        modifiled = grinder.exposure(image, 0.5, 30)
        modifiled = grinder.sharpen(modifiled)
        modifiled = grinder.blur(modifiled, 20)
        modifiled = grinder.make_noise(modifiled)

        # Show the results.
        print(tokens)
        cv2.imshow('result', image)
        cv2.imshow('modified', modifiled)
        if cv2.waitKey(100) == 27:
            break
