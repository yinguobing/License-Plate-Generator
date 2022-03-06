"""According to The License Plates of Motor Vehicles of the People's Republic
of China, GA36-2018."""
from itertools import chain

# BLANK means an absence of a token.
BLANK = ['-']

# Provinces
PROVINCES = ['京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪', '苏', '浙', '皖',
             '闽', '赣', '鲁', '豫', '鄂', '湘', '粤', '桂', '琼', '渝', '川', '贵',
             '云', '藏', '陕', '甘', '青', '宁', '新']

# Alphabets
ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Digits
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Appendix
APPENDIX = ['挂', '警', '学', '使', '领', '港', '澳']

# A collection of all license characters. Note the first one MUST be the BLANK
# token.
FULLSET = chain(
    BLANK,
    PROVINCES,
    ALPHABETS,
    DIGITS,
    APPENDIX,
)
