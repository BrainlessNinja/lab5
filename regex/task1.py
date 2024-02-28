import re

test = ["a", "ab", "abb", "aba", "bbb"]

expression = r'a+b*'

for x in test:
    if re.fullmatch(expression, x):
        print(f"{x} match")
    else:
        print(f"{x} not match")