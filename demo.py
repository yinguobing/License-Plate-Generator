"""Generate random license plate images."""
import cv2

import tokens
from license_plate import LPImageGenerator, TokenSet

if __name__ == "__main__":
    # What the license would be like?
    mixed = tokens.ALPHABETS
    mixed.extend(tokens.DIGITS)
    targets = [
        tokens.PROVINCES, tokens.ALPHABETS, mixed, mixed, mixed, mixed, mixed
    ]

    # What are the locations for each token character?
    locations = [
        (15, 25),
        (72, 25),
        (151, 25),
        (208, 25),
        (265, 25),
        (322, 25),
        (379, 25),
    ]

    assert len(targets) == len(
        locations), f"字符长度{len(targets)}与位置长度{len(locations)}不一致。"

    # Where is the background imagefile?
    background_file = 'assets/background/blue/140.png'

    # Where are the token image files?
    token_dir = 'assets/tokens/condensed-0'

    # The generator.
    token_sets = [TokenSet(chars, token_dir) for chars in targets]
    generator = LPImageGenerator(token_sets, background_file, locations)

    # Generate some license plates.
    for _ in range(5):
        result = generator.random_generate()

        # Show the results.
        cv2.imshow('result', result)
        cv2.waitKey(0)
