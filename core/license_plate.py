"""License plate number generation."""
import cv2

import core.pixel as pixel
from core.token import TokenSet


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
        self._valid_tokens = TokenSet(
            pattern.valid_token_set, pattern.token_img_dir)

        # How to convert all the tokens into a unique ID?
        self._token_dict = {c: i for i, c in enumerate(self._full_token_chars)}

    def _to_image(self, token_list):
        """Convet the input chars into image.

        Args:
            token_list: a list or tokens.
        """
        pseudo_plate = self._background.copy()
        token_str = ''
        for token, location, color in zip(token_list, self._locations, self._colors):
            mask = pixel.img_to_mask(token.image, reverse=True)
            pseudo_plate = pixel.overlay(pseudo_plate, mask, location, color)
            token_str += token.char

        return pseudo_plate, token_str

    def random_generate(self):
        """Generate a piece of random license with the current token."""
        tokens = [t.get_random_one()
                  for t in self._token_sets.get_random_one()]
        return self._to_image(tokens)

    def generate(self, chars):
        """Generate a license plate with given chars.

        Args:
            chars: a list of characters or a string as license number.
        """
        tokens = [self._valid_tokens.get(c) for c in chars]
        return self._to_image(tokens)

    def generate_with_char_sets(self, char_set_list, token_img_dir):
        """Generate a license plate with given char set list.

        Args:
            char_set_list: a list of chars sets
            token_img_dir: the token image directory
        """
        token_set_list = [TokenSet(chars, token_img_dir)
                          for chars in char_set_list]
        tokens = [t.get_random_one() for t in token_set_list]
        return self._to_image(tokens)
