import re

def camel_to_snake(text):
  return re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()

camel_case_string = "HelloWorld"
snake_case_string = camel_to_snake(camel_case_string)
print(snake_case_string)  # Output: hello_world
