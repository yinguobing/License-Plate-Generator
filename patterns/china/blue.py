"""According to The License Plates of Motor Vehicles of the People's Republic
of China, GA36-2018."""
import random
from itertools import chain

import patterns.china.tokens as tokens
from core.pattern import Pattern
from core.token import TokenSet

# 蓝牌140

# 一个车牌包含几个字符？
size = 7

# 每一位字符可以使用的的字符组
mixed = list(chain(tokens.REDUCED_ALPHABETS, tokens.DIGITS))
targets = [tokens.PROVINCES, tokens.ALPHABETS,
           mixed, mixed, mixed, mixed, mixed]

# 每一位字符的位置：左上角的像素坐标
locations = [(15, 25), (72, 25), (151, 25), (208, 25),
             (265, 25), (322, 25), (379, 25)]

# 每一位字符的颜色(BGR)
colors = [(255, 255, 255), (255, 255, 255), (255, 255, 255),
          (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]

# 字符图像的存储位置
token_img_dir = 'assets/tokens/condensed-0'

# 背景图像的路径
background_file = 'assets/background/blue/140.png'

assert len(targets) == size, f"Token长度{len(targets)}不等于{size}。"
assert len(locations) == size, f"位置长度{len(locations)}不等于{size}。"
assert len(colors) == size, f"色彩长度{len(colors)}不等于{size}。"


class BlueTokenSets:

    def __init__(self) -> None:
        self.token_sets = [TokenSet(tokens.PROVINCES, token_img_dir),
                           TokenSet(tokens.ALPHABETS, token_img_dir)]

        # There should be no more than 2 letters in a valid license.
        self.series = [tokens.REDUCED_ALPHABETS,
                       tokens.REDUCED_ALPHABETS,
                       tokens.DIGITS,
                       tokens.DIGITS,
                       tokens.DIGITS]

    def get_random_one(self):
        series = self.series.copy()
        random.shuffle(series)
        token_sets = self.token_sets.copy()
        token_sets.extend([TokenSet(chars, token_img_dir) for chars in series])

        return token_sets


BLUE = Pattern(
    name='blue',
    token_count=size,
    token_sets=BlueTokenSets(),
    full_token_chars=tokens.FULLSET,
    background_file=background_file,
    token_locations=locations,
    token_colors=colors,
    token_img_dir=token_img_dir,
    valid_token_set=list(
        chain(tokens.PROVINCES, tokens.ALPHABETS, tokens.DIGITS))
)
