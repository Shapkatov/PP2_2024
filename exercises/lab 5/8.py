import re

text = "MyNameIsKhamid"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)