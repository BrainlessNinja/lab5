import re

unwanted_specialchr = [',', '.', ' ']
string = "a,bhc.kalaej jff"
print(re.sub(f'[{"".join(unwanted_specialchr)}]', ':', string))
