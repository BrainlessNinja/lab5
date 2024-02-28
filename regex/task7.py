import re

def snake_to_camel(text):
  return ''.join(word.capitalize() for word in re.split('_(?=[a-z])', text))

snake_case_string = "hello_world"
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)