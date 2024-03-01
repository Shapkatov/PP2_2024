import re

text = "Hello My name, is. Khamid"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)