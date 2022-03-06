"""According to The License Plates of Motor Vehicles of the People's Republic
of China, GA36-2018."""
from itertools import chain

import patterns.china.tokens as tokens
from core.pattern import Pattern
from core.token import TokenSet

# 绿140

# 一个车牌包含几个字符？
size = 8

# 每一位字符可以使用的的字符组
mixed = list(chain(tokens.ALPHABETS, tokens.DIGITS))
targets = [tokens.PROVINCES, tokens.ALPHABETS,
           mixed, mixed, mixed, mixed, mixed, mixed]

# 每一位字符的位置：左上角的像素坐标
locations = [(15, 25), (69, 25), (161, 25), (213, 25),
             (265, 25), (317, 25), (369, 25), (421, 25)]

# 每一位字符的颜色(BGR)
colors = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
          (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

# 字符图像的存储位置
token_img_dir = 'assets/tokens/condensed-1'

# 背景图像的路径
background_file = 'assets/background/green/140-B.png'

assert len(targets) == size, f"Token长度{len(targets)}不等于{size}。"
assert len(locations) == size, f"位置长度{len(locations)}不等于{size}。"
assert len(colors) == size, f"色彩长度{len(colors)}不等于{size}。"

GREEN_B = Pattern(
    token_count=7,
    token_sets=[TokenSet(chars, token_img_dir) for chars in targets],
    full_token_chars=tokens.FULLSET,
    background_file=background_file,
    token_locations=locations,
    token_colors=colors)
