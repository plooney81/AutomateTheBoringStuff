import re

# #? Basics
# phoneNumbRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phoneNumbRegex.search('My number is 713-592-0119')
# print(mo.group())

# #? Grouping
# phoneNumbRegex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# mo2 = phoneNumbRegex2.search('My number is 713-592-0119')
# print(mo2.group(1)) # prints the first "group" i.e. pattern inside the first set of ()
# print(mo2.group(2)) # prints the second
# print(mo2.group(0)) # prints the whole match
# print(mo2.group()) # also prints the whole match

# print(mo2.groups()) # prints each group match seperated by commas
# areaCode, otherNumber = mo2.groups()
# print(areaCode)
# print(otherNumber)

# #? Escaping char in regex
# phoneNumbRegex3 = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
# mo3 = phoneNumbRegex3.search('My number is (713)-592-0119')
# areaCode, otherNumber = mo3.groups()
# print(f'{areaCode} {otherNumber}')

# #? Multiple groups with the pipe "|" character
# regex4 = re.compile(r'Batman|Robin')
# mo4 = regex4.search('Batman')
# mo5 = regex4.search('Robin')
# mo6 = regex4.search('Batman and Robin') # returns the first match if both are true
# print(mo4.group())
# print(mo5.group())
# print(mo6.group())

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo_bat = batRegex.search('Batmobile was in a horrible crash')
# print(mo_bat.group())
# print(mo_bat.group(1))

# #? Optional Matching with the ?
# batRegex2 = re.compile(r'Bat(wo)?man')
# mo_optional1 = batRegex2.search('Are Batman and the Joker secret friends?')
# print(mo_optional1.group())
# mo_optional2 = batRegex2.search('Are Batwoman and the Robin secret friends?')
# print(mo_optional2.group())

# anotherNumberRegex = re.compile(r'(\d{3}-)?(\d{3}-\d{4})')
# mo_anotherNumb1 = anotherNumberRegex.search('my number is 713-592-0119')
# mo_anotherNumb2 = anotherNumberRegex.search('my number is 592-0119')
# print(mo_anotherNumb1.group())
# print(mo_anotherNumb2.group())

# #? Matching zero or more w/ *
anotherBatRegex = re.compile(r'Bat(wo)*man')
sentencess = ['The adventures of Batman', 'The adventures of Batwoman', 'The adventures of Batwowowowoman']
for sentence in sentencess:
    print(sentence)
    mo = anotherBatRegex.search(sentence)
    print(mo.group())