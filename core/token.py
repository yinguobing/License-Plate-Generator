import os
from collections import namedtuple
from random import choice

import cv2

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

    def get(self, char):
        """Return a token of char."""
        return self.data.get(char)

    def get_random_one(self):
        """Return a random token from the current set."""
        return self.data.get(choice(self.chars))

    def get_image(self, char=None):
        """Return the token image of a given character. Return None if not found."""
        token = self.data.get(char)
        if token is None:
            return None
        return token.image
