"""According to The License Plates of Motor Vehicles of the People's Republic
of China, GA36-2018."""
from collections import namedtuple
from itertools import chain

import tokens
from license_plate import TokenSet

Pattern = namedtuple(
    'Pattern', ['size', 'background_file', 'token_sets', 'locations'])

# 蓝牌140

# 一个车牌包含几个字符？
SIZE = 7

# 每一位字符可以使用的的字符组
mixed = list(chain(tokens.ALPHABETS, tokens.DIGITS))
targets = [tokens.PROVINCES, tokens.ALPHABETS,
           mixed, mixed, mixed, mixed, mixed]

# 每一位字符的位置：左上角的像素坐标
locations = [(15, 25), (72, 25), (151, 25), (208, 25),
             (265, 25), (322, 25), (379, 25)]

# 字符图像的存储位置
token_dir = 'assets/tokens/condensed-0'

# 背景图像的路径
background_file = 'assets/background/blue/140.png'

assert len(targets) == SIZE, f"Token长度{len(targets)}不等于{SIZE}。"
assert len(locations) == SIZE, f"位置长度{len(targets)}不等于{SIZE}。"

BLUE = Pattern(
    size=7,
    background_file=background_file,
    token_sets=[TokenSet(chars, token_dir) for chars in targets],
    locations=locations)
