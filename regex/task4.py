import re

test = "Hello World hello world"

expression = r'[A-Z][a-z]+'


sequence = re.findall(expression, test)


print("Found:")
for x in sequence:
    print(x)