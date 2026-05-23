import re

pattern= re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')


emails=""" 
adiexplainsofficial@gmail.com
adi.explains@youtube.net
adi-321-explains@workmail.com
"""


text_sample=""" 
983.932.2342
100-200-3000
200-100-3000


Mr. Aditya
Ms Andrea
Mr. Ramesh
Ms Smith
Mr Suresh


"""

text=emails

matches = pattern.finditer(text)
for match in matches:
     print(match)



















