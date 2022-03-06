"""According to The License Plates of Motor Vehicles of the People's Republic
of China, GA36-2018."""
from itertools import chain

import patterns.china.tokens as tokens
from core.pattern import Pattern
from core.token import TokenSet

# 教练汽车140

# 一个车牌包含几个字符？
size = 7

# 每一位字符可以使用的的字符组
mixed = list(chain(tokens.ALPHABETS, tokens.DIGITS))
targets = [tokens.PROVINCES, tokens.ALPHABETS,
           mixed, mixed, mixed, mixed, ['警']]

# 每一位字符的位置：左上角的像素坐标
locations = [(15, 25), (92, 25), (151, 25), (208, 25),
             (265, 25), (322, 25), (379, 25)]

# 每一位字符的颜色(BGR)
colors = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0),
          (0, 0, 0), (0, 0, 0), (20, 37, 228)]

# 字符图像的存储位置
token_img_dir = 'assets/tokens/condensed-0'

# 背景图像的路径
background_file = 'assets/background/white/140.png'

assert len(targets) == size, f"Token长度{len(targets)}不等于{size}。"
assert len(locations) == size, f"位置长度{len(locations)}不等于{size}。"
assert len(colors) == size, f"色彩长度{len(colors)}不等于{size}。"

WHITE = Pattern(
    token_count=7,
    token_sets=[TokenSet(chars, token_img_dir) for chars in targets],
    full_token_chars=tokens.FULLSET,
    background_file=background_file,
    token_locations=locations,
    token_colors=colors)
