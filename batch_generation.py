"""Generate random license plate images."""
import os

import cv2
from tqdm import tqdm

from core.license_plate import LPImageGenerator
from patterns.china import (BLUE, CONSULATE, DRIVING_SCHOOL, EMBASSY, GREEN_A,
                            GREEN_B, HONGKONG, MACAO, WHITE, YELLOW)


def generate(pattern, target_dir, num_samples):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # What the license would be like?
    generator = LPImageGenerator(pattern)

    # Generate some license plates.
    for i in tqdm(range(num_samples)):
        img, license_str = generator.random_generate()

        # Write to disk.
        img_file_name = f'{pattern.name}_{i:06d}_{license_str}.jpg'
        cv2.imwrite(os.path.join(target_dir, img_file_name), img)


if __name__ == "__main__":
    # What kind of license plate will be generated?
    patterns = (BLUE, CONSULATE, DRIVING_SCHOOL, EMBASSY, GREEN_A,
                GREEN_B, HONGKONG, MACAO, WHITE, YELLOW)

    for pattern in patterns:
        print(f"Generating {pattern.name} licenses...")

        # Where will the generated images be stored?
        target_dir = '/home/robin/data/glpi'
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # How many images should be generated?
        num_samples = 100000

        # Run generations
        generate(pattern, target_dir, num_samples)
