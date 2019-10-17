import sys, re
from tkinter import Tk

text = sys.argv[1]

#main replacement
text = text.lower().replace(' ', '-')

#only alphanumeric chars, '_' and '-' allowed
text = re.sub(r'[^\w-]+', '', text)

r = Tk()
r.clipboard_clear()
r.clipboard_append(text)
r.update()

print(text)