import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.findall('My number is 415-555-4242. 415-555-4342')
print('Phone number found: ' + mo[1])