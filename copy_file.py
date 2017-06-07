import shutil, send2trash, os, zipfile

#shutil.copy('data.py', './radom/sfds.py')
# 遍历目录树  1.当前文件夹名称的字符串;2.当前文件夹中子文件夹的字符串的列表。3.当前文件夹中文件的字符串的列表。
for fname, subfs, filenames in os.walk('/Users/wubo/Downloads'):
    print('1 the current folder is:' + fname)
    # for subf in subfs:
    #     print('1.1 sub folder of ' + fname + ':' +subf)
    for filename in filenames:
        print('1.2 file inside of ' + fname + ':' + filename)