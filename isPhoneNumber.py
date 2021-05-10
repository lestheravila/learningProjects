def isPhoneNumber(text):
    if len(text) != 12: #1
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():#2
            return False
    if text[3] != '-':#3
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():#4
            return False
    if text[7] != '-':#5
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():#6
            return False
    return True#7
    
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
