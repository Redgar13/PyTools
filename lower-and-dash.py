import sys, re

text = sys.argv[1]

#main replacement
text = text.lower().replace(' ', '-')

#only alphanumeric chars, '_' and '-' allowed
text = re.sub(r'[^\w-]+', '', text)

print(text)