import pyperclip
import sys

"""
?This program excepts a command line argument
?If the argument text matches that of the dictionary, then we copy the value related
?To the key in the dictionary to the computer clipboard
"""

text = {
    'agree' : """Yes, I agree. That sounds find to me.""",
    'busy' : """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?"""
}

if len(sys.argv) < 2:
    print('Usage: python Multi-Clipboard.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1].lower() #First command line argument is the keyphrase, i.e. agree, busy, or upsell

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f'Text for keyphrase {keyphrase} copied to the clipboard')
else:
    print('Invalid keyphrase')