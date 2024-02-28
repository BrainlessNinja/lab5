import re

def match_pattern(text, pattern):
  return bool(re.search(pattern, text))

pattern = r"a.b"

text1 = "This is a string with an ab at the end."
text2 = "This has no match."
text3 = "aab"

print(f"Text1: {match_pattern(text1, pattern)}")
print(f"Text2: {match_pattern(text2, pattern)}")
print(f"Text3: {match_pattern(text3, pattern)}")
