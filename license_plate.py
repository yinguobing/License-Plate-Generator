"""License plate number generation."""
import os
from collections import namedtuple
from random import choice

import cv2

import pixels
import tokens

Token = namedtuple('Token', 'char image')


class TokenSet:
    """A collection of tokens."""

    def __init__(self, token_chars: list, img_dir: str) -> None:
        """Create a toke set from input characters."""
        self.chars = token_chars
        self.data = {}
        for c in self.chars:
            img_file = os.path.join(img_dir, f'{c}.jpg')
            assert os.path.exists(
                img_file), f"Token image file not found: {img_file}"
            img = cv2.imread(img_file)
            self.data.update({c: Token(c, img)})

    def get_random_one(self):
        """Return a random token from the current set."""
        return self.data.get(choice(self.chars))

    def get_image(self, char=None):
        """Return the token image of a given character. Return None if not found."""
        token = self.data.get(char)
        if token is None:
            return None
        return token.image


class LPImageGenerator:
    """License plate image generator."""

    def __init__(self,
                 token_sets: list,
                 background_file: str,
                 locations: list) -> None:
        """Create a license plate image generator."""
        # What kind of license should be generated?
        self._token_sets = token_sets
        self._background = cv2.imread(background_file)
        self._locations = locations

        # How to convert all the tokens into a unique ID?
        self._token_dict = {c: i for i, c in enumerate(tokens.FULLSET)}

    def random_generate(self):
        """Generate a piece of random license with the current token."""
        pseudo_plate = self._background.copy()
        for token_set, location in zip(self._token_sets, self._locations):
            token = token_set.get_random_one()
            mask = pixels.img_to_mask(token.image, reverse=True)
            pseudo_plate = pixels.overlay(
                pseudo_plate, mask, location, (255, 255, 255))

        return pseudo_plate
