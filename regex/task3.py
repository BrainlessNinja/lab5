import re

string1 = "Hello wor_ld hello_world world_hello hell_o_wor_ld_world_world_world."


sequence = re.findall(r'\b[a-z]+(?:_[a-z]+)+\b', string1)

print("Found:")
for x in sequence:
    print(x)