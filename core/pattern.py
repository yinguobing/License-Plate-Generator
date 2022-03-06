from collections import namedtuple

Pattern = namedtuple(
    'Pattern', [
        # How many tokens does one license have?
        'token_count',

        # A list of TokenSet, each element is a valid set of tokens for current location.
        'token_sets',

        # A list of all the token characters, including the blank '-'.
        'full_token_chars',

        # The top left corner of the token images in the background coordinates.
        'token_locations',

        # A list of color tuple (B,G,R) for each token.
        'token_colors',

        # The background image file.
        'background_file',
    ]
)
