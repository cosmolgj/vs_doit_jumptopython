data = """
park 800905-1049128
kim  701019-2018421
"""

result = []

for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))


import re

data = """
park 800905-1049128
kim  701019-2018421
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))


p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one 
life is too short
python two
you need python
python three"""

print(p.findall(data))


def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65029 for printing, 29384 for user code.'))
