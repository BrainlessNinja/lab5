import re

def insert_spaces(text):
  return re.sub(r"(?<!\s)([A-Z])", r" \1", text)

text = "ThisIsAStringWithNoSpaces"
spaced_text = insert_spaces(text)
print(spaced_text)  # Output: This Is A String With No Spaces
