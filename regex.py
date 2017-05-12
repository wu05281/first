#!/usr/bin/python
# -*- coding: utf-8 -*-
#Python编程快速上手让繁琐工作自动化  第七章 学习
#re.compile创建Regex对象，通过调用Regex对象的search，findall方法，获取Marcher对象，
#search方法： Marcher对象的group返回第一次匹配的字符串，groups返回匹配的分组信息。
#findall方法：没有分组，Marcher对象的group返回所有匹配的字符串列表；有分组，返回字符串的元组列表
import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|\.|-)?
    (\d{3})
    (\s|\.|-)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

email_regex = re.compile('''(([a-zA-Z0-9_.-]+)
    @
    ([a-zA-Z0-9.-]+)
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_number += ' X' + groups[8]
    matches.append(phone_number)

for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

###800-420-7240
#415-863-9900
#415-863-9950
#info@nostarch.com
#media@nostarch.com
#academic@nostarch.com
#help@nostarch.com