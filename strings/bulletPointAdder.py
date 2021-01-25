import pyperclip
"""
?Returns the text copied in the clipboard with bullet points in front of it
"""

text = pyperclip.paste()
text = text.split('\n')
for i, newLine in enumerate(text): text[i] = '* ' + text[i]

text = '\n'.join(text)
pyperclip.copy(text)