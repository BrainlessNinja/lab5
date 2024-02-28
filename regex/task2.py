import re

test = ["a", "ab", "aba", "abb", "abbb", "aaaa"]


expression = r'a+b{2,3}'

for x in test:
    if re.fullmatch(expression, x):
        print(f"{x} match")
    else:
        print(f"{x} not match")