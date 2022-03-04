"""License plate number generation."""
import itertools
from random import choice

from tokens import FULLSET


class Pattern:
    """A pattern defines what a license place looks like."""

    def __init__(self, token_sets) -> None:
        """Create a license pattern object.

        Args:
            token_sets: a list of token sets of the same size. Multiple token
                sets could be grouped in a list as a single set.
        """
        self.token_sets = token_sets


class LPImageGenerator:
    """License plate image generator."""

    def __init__(self, pattern: Pattern) -> None:
        """Create a license plate image generator."""
        # What kind of license should be generated?
        self._pattern = pattern
        self._token_set_list = []
        for token_set in self._pattern.token_sets:
            if type(token_set) is list:
                self._token_set_list.append(list(itertools.chain(*token_set)))
            else:
                self._token_set_list.append(token_set)

        # How to convert all the tokens into a unique ID?
        self._token_dict = {t: i for i, t in enumerate(FULLSET)}

    def random_generate(self):
        """Generate a piece of random license with the current token.

        Returns:
            license: a list of token ids.
            license_str: the license string.
        """
        license = []
        license_str = ''
        for _tokens in self._token_set_list:
            char = choice(_tokens)
            license_str += char
            token_id = self._token_dict[char]
            license.append(token_id)

        return license, license_str
