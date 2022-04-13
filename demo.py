"""Generate random license plate images."""
from random import randint, random

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

    # Generate a license plate from specific number.
    image, tokens = generator.generate('晋H99999')
    cv2.imshow('result', image)
    cv2.waitKey()

    # Generate a license plate from manually selected characters.
    image, tokens = generator.generate_with_char_sets(
        [['粤', '京'],
         ['A', 'Z'],
         ['B', 'C'],
         ['1', '3'],
         ['2', '4'],
         ['X', 'H'],
         ['0', '8']], 'assets/tokens/condensed-0'
    )
    cv2.imshow('result', image)
    cv2.waitKey()

    # Generate some license plates.
    for _ in range(100):

        # Generate one license plate.
        image, tokens = generator.random_generate()

        # Grind it!
        modifiled = image.copy()
        modifiled = grinder.exposure(image, 0.3 + random(), 50*random())
        modifiled = grinder.sharpen(modifiled)
        modifiled = grinder.blur(modifiled, randint(1, 6)*2 + 1)
        modifiled = grinder.make_noise(modifiled, 0, 0.01)

        # Show the results.
        print(tokens)
        cv2.imshow('result', image)
        cv2.imshow('modified', modifiled)
        if cv2.waitKey(100) == 27:
            break
