import re

text= """abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Metacharacters: . ^ $ * + ? { } [ ] /| ( )
adiexplains.com

983-932-2342
343-342-1232
454.932.2342
423*324*2434
342--423--3245

100-423-5435
200-523-5325

abcgdfgdfhfd
Ta TaTa

cat
bat
sat
rat
tat

 """

# sentence = "The rain in Spain stays mainly in the plain"

pattern = re.compile(r'[^r]at')

matches = pattern.finditer(text)
for match in matches:
     print(match)

# simple example matching abc
# Show matching period '.'
# show matching "adiexplains.com"
# Explain the operators
# show matching phone numbers with . '\d' and '\d{3}', use charater set [.-]
# show matching phone numbers with '-' and '.'
# show -- does not match
# show matching 100, 200
# matching between a range [1-5], [a-zA-Z]
# Show negate character set [^a-zA-Z0-9], [^c]at
# Go back to phone number example to explain quantifiers
# show matching the names in a sentence
# show matching an email
# show how to read a regex written by others