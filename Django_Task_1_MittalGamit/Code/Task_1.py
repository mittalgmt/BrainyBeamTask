import re

str = "Layla is a good data scientist"

pattern = r'\b\w*a\w*a\w*\b'

matches = re.findall(pattern, str)

result = [word for word in matches if word.count('a') == 2]

print(result)
