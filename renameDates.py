import shutil, os, re

datePattern = re.compile(r'''^(.*?)#任意字符开头
    ((?:0[1-9])|(?:1[012]))-#01/1-12  月份
    (0[1-9]|[12][0-9]|3[01])-#日期
    ((?:19|20)\d\d)#年
    (.*?)$''', re.VERBOSE)  # re.VERBOSE这将在正则表达式字符串中允许空白字符和注释，让它更可读。
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo is None:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2) #月份
    dayPart = mo.group(3)   #日期
    yearPart = mo.group(4)  #年
    afterPart = mo.group(5)
    print(beforePart + yearPart + monthPart + dayPart + afterPart)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    # shutil.move(amerFilename, euroFilename) # uncomment after testing
