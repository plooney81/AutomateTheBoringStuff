#!/usr/bin/python3
import pyinputplus as pyip
from pathlib import Path
from readmeIcons import readMeIcons

#? Creates a readme file for a user in a specified position

#? getPath Function
#* Function that gets the user path and checks if its valid
def getPathAndCheck():
    while True:
        print('\nEnter directory path:')
        userInput = Path(input('> '))
        if userInput.is_dir():
            return userInput
        print('Invalid Path. Must be an absolute path to a valid directory\n')

#? getTitle Function
#* function that asks if the user wants to change the title of the ReadmeFile
def getTitle(default):
    print(f'\nDefault readme title: {default}\nPress enter to keep default, or type your title change:')
    userInput = input('> ')
    return default if userInput == '' else userInput

#? getLanguages Function
#* function that asks the user for a list of Languages used
def getLanguages():
    possibleLanguages = list(readMeIcons['Programming Languages'].keys())
    chosenLanguages = []
    print(f'\nEnter the languages used for the project')
    listOptions(possibleLanguages, 0, 'Languages')
    while True:
        userInput = input('\nType d if done, l to see list, or type in language name (case sensitive)\n> ')
        if userInput.lower() == 'd':
            return chosenLanguages
        elif userInput.lower() == 'l':
            if len(chosenLanguages) == 0:
                listOptions(possibleLanguages, 0, 'Languages')
            else:
                listOptions(possibleLanguages, 1, 'Languages')
        elif userInput in possibleLanguages:
            chosenLanguages.append(userInput)
            del possibleLanguages[possibleLanguages.index(userInput)]
        else:
            print('Whoops not available.')

#? getFrameworks Function
#* function that asks the user for a list of frameworks used
def getFrameworks():
    possibleFrameworks = list(readMeIcons['Frameworks'].keys())
    chosenFrameworks = []
    print(f'\nEnter the frameworks used for the project')
    listOptions(possibleFrameworks, 0, 'Frameworks')
    while True:
        userInput = input('\nType d if done, l to see list, or type in language name (case sensitive)\n> ')
        if userInput.lower() == 'd':
            return chosenFrameworks
        elif userInput.lower() == 'l':
            if len(chosenFrameworks) == 0:
                listOptions(possibleFrameworks, 0, 'Frameworks')
            else:
                listOptions(possibleFrameworks, 1, 'Frameworks')
        elif userInput in possibleFrameworks:
            chosenFrameworks.append(userInput)
            del possibleFrameworks[possibleFrameworks.index(userInput)]
        else:
            print('Whoops not available.')

#? listOptions Function
#* function that takes a name, list and integer and lists out the values of the list
def listOptions(possibleOptions, i, name):
    printString = ''
    if i == 0:
        print(f'Here is a list of {name} we support:\n')
    else:
        print(f'Here is the updated list of {name}:\n')
    for i, option in enumerate(possibleOptions):
        if i == 0:
            printString += f'{option}'
        else:
            printString += f', {option}'
    print(printString)

#? getReadmeIcons Function
#* takes a list of keys and another string value that decides which icons to choose between, returns a string of all the icons
def getReadmeIcons(listOfKeys, languagesOrFrameworks):
    returnString = ''
    for key in listOfKeys:
        returnString += readMeIcons[languagesOrFrameworks][key]
    return returnString

# todo ask for contributor information
# todo including, GitHub and LinkedIn url's for each contributor
#? getContributors Function
#* asks if they would like to add a user
#* if yes, add user name, github link, linkedIn link
#* if no, exit
def getContributors():
    possibleSocial = list(readMeIcons['Social'].keys())
    contributors = []
    while True:
        print(f'\nAdd a contributor to the project? Y or N')
        userInput = input('\n> ')
        if userInput.lower() == 'y':
            newContributor = {}
            name = input(f'\nContributor name:\n> ').title()
            for social in possibleSocial:
                link = input(f'\nEnter link to {name}\'s {social} profile\n> ')
                if link != '':
                    newContributor[social] = link
            newContributor['name'] = name
            contributors.append(newContributor)
        elif userInput.lower() == 'n':
            return contributors
        else:
            print('Whoops not an option')

def getContributorIcons(contributors):
    returnString = ''
    for contributor in contributors:
        contributorString = ''
        contributorString += f"* {contributor['name']} "
        for key in contributor:
            if key != 'name' and (key in readMeIcons['Social']):
                contributorString += f"<a href='{contributor[key]}'>"
                contributorString += readMeIcons['Social'][key]
                contributorString += "</a>"
        returnString += contributorString + '\n'
    return returnString


# todo get a brief project description
#? getDescription Function
#* asks user for a general description of the project

# todo get stretch goals information
#? getStretchGoals Function
#* asks user if they have any stretch goals

p = getPathAndCheck()
title = getTitle(p.stem.title())
languages = getLanguages()
frameworks = getFrameworks()
languagesReadmeIcons = getReadmeIcons(languages, 'Programming Languages')
frameworksReadmeIcons = getReadmeIcons(frameworks, 'Frameworks')
contributors = getContributors()
print(getContributorIcons(contributors))


# readmeFile = open(p / f'{p.stem}_generated_README.md', 'w')






# template = f"""
# ### {title}
# - [**General**](#general)
#   - [Technology and Frameworks Used:](#technology-and-frameworks-used)
#   - [Project Contributors:](#project-contributors)
# - [How To Use:](#how-to-use)
#   - [Signup/Login](#signuplogin)
#   - [Navigating the ___ Feature](#navigating-the-___-feature)
#   - [Using the ___ feature](#using-the-___-feature)

# <hr>

# ## **General**
# - {generalAboutText}
# <!--  -->

# ### Technology and Frameworks Used:

# <div>
#     <h2>Languages Used</h2>
#     {languagesText}
# </div>
# <div>
#     <h2>Frameworks & Additional Technologies Used</h2>
#     {frameworksText}
# </div>
  

# ### Project Contributors:
# * Peter Looney <a href='https://github.com/plooney81'>
#                   <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>
#                 </a>
#                 <a href='https://www.linkedin.com/in/peter-looney-27b732166/'>
#                   <img src="https://img.shields.io/badge/linkedin%20-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
#                 </a>
# <!-- * Insert project contributors -->
# {projectContributorsText}

# <hr>


# ## How To Use:

# ### Signup/Login


# ### Navigating the ___ Feature


# ### Using the ___ feature
   
# """