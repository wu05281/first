
import re

numRegex = re.compile(r'\d{1,2},\d{3}')
result = numRegex.search('23,12')

#oo = re.match(r'\d{1,2}(,\d{3})*$', '2,345')
oo = re.match(r'^[A-Z][a-z]+\sNakamoto$', 'Nakamoto')
if oo:
    print('ok')
else:
    print('no')


#密码强度检查正则表达式
pwc = re.match(r'''
    (?=^.{8,18}$)                        #长度高于八位
    (?=(?:.*?\d){1})                     #至少包含一位数字
    (?=.*[a-z])                          #至少一位小写字母
    (?=(?:.*?[A-Z]){1})                  #至少一位大写字母
    (?=(?:.*?[!@#$%*()_+^&}{:;?.]){1})   #至少一位特殊字符'!@#$%*()_+^&}{:;?.'
    (?!.*\s)                             #不包含任何空格
    [0-9a-zA-Z!@#$%*()_+^&]*$            
    ''', 'sffs@800909W', re.VERBOSE)
if pwc:
    print('ok')
else:
    print('no')


