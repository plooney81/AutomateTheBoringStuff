import pyperclip
import sys

"""
?This program excepts a command line argument
?If the argument text matches that of the dictionary, then we copy the value related
?To the key in the dictionary to the computer clipboard
"""
readmeStarter = """
- [**General**](#general)
  - [Technology and Frameworks Used:](#technology-and-frameworks-used)
  - [Project Contributors:](#project-contributors)
- [How To Use:](#how-to-use)
  - [Signup/Login](#signuplogin)
  - [Navigating Chat Groups](#navigating-chat-groups)
  - [Sending Messages and Code Snippets](#sending-messages-and-code-snippets)
  - [Changing Profile Information](#changing-profile-information)

<hr>

## **General**

![Javascript](https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML](https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white)

### Technology and Frameworks Used:

![React](https://img.shields.io/badge/react%20-%2320232a.svg?&style=for-the-badge&logo=react&logoColor=%2361DAFB)![Redux](https://img.shields.io/badge/redux%20-%23593d88.svg?&style=for-the-badge&logo=redux&logoColor=white)
![Firebase](https://img.shields.io/badge/firebase%20-%23039BE5.svg?&style=for-the-badge&logo=firebase)
![Bootstrap](https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white)
  

### Project Contributors:
* Peter Looney <a href='https://github.com/plooney81'><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/></a><a href='https://www.linkedin.com/in/peter-looney-27b732166/'><img src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/></a>

<hr>

<!-- Explain how the project works:
* Include some code snippets -->

## How To Use:

### Signup/Login


### Navigating the ___ Feature


### Using the ___ feature
   

### Changing Profile Information

"""

text = {
    'agree' : """Yes, I agree. That sounds find to me.""",
    'busy' : """Sorry, can we do this later this week or next week?""",
    'upsell': """Would you consider making this a monthly donation?""",
    'readme': readmeStarter
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