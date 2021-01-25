"""
? Piglatin - asks user for input and converts to piglatin
"""

print('Enter an english phrase that you would like to be converted to pig-latin')
response = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

piglatin = []
for word in response.split():

    preFixNonLetters = ''
    #isalpha returns true of the string consists of letters and consist of only letters
    while len(word) > 0 and not word[0].isalpha(): 
        preFixNonLetters += word[0]
        word = word[1:]
        if len(word) == 0:
            piglatin.append(preFixNonLetters)
        
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    
    wasUpper = word.isupper() #checks if all of the characters in the word were uppercase
    wasTitle = word.istitle() #checks if the first letter of the word was uppercase

    word = word.lower()

    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    piglatin.append(preFixNonLetters + word + suffixNonLetters)

print(' '.join(piglatin))