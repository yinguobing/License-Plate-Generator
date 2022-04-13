"""License plate number generation."""
import cv2

import core.pixel as pixel


class LPImageGenerator:
    """License plate image generator."""

    def __init__(self, pattern) -> None:
        """Create a license plate image generator."""
        # What kind of license should be generated?
        self._token_sets = pattern.token_sets
        self._background = cv2.imread(
            pattern.background_file, cv2.IMREAD_UNCHANGED)
        self._locations = pattern.token_locations
        self._colors = pattern.token_colors
        self._full_token_chars = pattern.full_token_chars

        # How to convert all the tokens into a unique ID?
        self._token_dict = {c: i for i, c in enumerate(self._full_token_chars)}

    def random_generate(self):
        """Generate a piece of random license with the current token."""
        pseudo_plate = self._background.copy()
        token_str = ''
        for token_set, location, color in zip(self._token_sets.get_random_one(), self._locations, self._colors):
            token = token_set.get_random_one()
            mask = pixel.img_to_mask(token.image, reverse=True)
            pseudo_plate = pixel.overlay(pseudo_plate, mask, location, color)
            token_str += token.char

        return pseudo_plate, token_str
