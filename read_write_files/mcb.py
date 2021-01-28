#!/usr/bin/python3

import sys, shelve, pyperclip

#? MultiClipboard Part 2 - Saves and loads pieces of text to the clipboard
#* .pyw extension means that Python won't show a Terminal window when it runs this program
#? USAGE: python3 mcb.py save <keyword> - Saves clipboard to keyword
#?        python3 mcb.py <keyword> - loads keyword to clipboard
#?        python3 mcb.py list - Loads all keywords to clipboard

def printUsage():
    print('Not enough arguments')
    print('python3 mcb.py save <keyword>')
    print('python3 mcb.py <keyword>')
    print('python3 mcb.py list')
    sys.exit()

if len(sys.argv) < 2: printUsage()
mcbShelf = shelve.open('mcb')


keyphrase = sys.argv[1].lower()

#? If first argument is save, grab the text from the clipboard
if len(sys.argv) == 3 and keyphrase == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #? Lists the keys in the shelve
    if keyphrase == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(pyperclip.paste())
    #? If key in shelf, copy to the clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f'Text for keyphrase {keyphrase} copied to the clipboard')
    else:
        printUsage()
else:
    printUsage()

mcbShelf.close()