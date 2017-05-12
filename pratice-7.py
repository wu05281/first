
import re

numRegex = re.compile(r'\d{1,2},\d{3}')
result = numRegex.search('23,12')

#oo = re.match(r'\d{1,2}(,\d{3})*$', '2,345')
oo = re.match(r'^[A-Z][a-z]+\sNakamoto$', 'Nakamoto')
if oo:
    print('ok')
else:
    print('no')