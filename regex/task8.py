import re

def split_at_uppercase(text):
  return re.findall(r'[A-Z][^A-Z]*', text)

text = "ThisIsAStringWithUppercaseLetters"
split_words = split_at_uppercase(text)
print(split_words)  # Output: ['This', 'Is', 'A', 'String', 'With', 'Uppercase', 'Letters']
