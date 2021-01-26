
#? Checks if the input is a valid phone number...
#? without using a Regular Expression
def is_phoneNumber(text):
    if len(text) != 12: return False
    for i in range(0, len(text)):
        if (i >= 0 and i <= 2) or (i >= 4 and i <= 6) or (i >= 8 and i <= 12):
            if not text[i].isdecimal(): return False
        else:
            if text[i] != '-': return False
    return True

print(is_phoneNumber('713-592-0119'))
print(is_phoneNumber(''))
print(is_phoneNumber('1111-111-111'))
print(is_phoneNumber('111-1111-111'))