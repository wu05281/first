import os, shutil, re


def choose_file(folder):
    folder = os.path.abspath(folder)
    # 生成备份文件夹
    number = 1
    while True:
        back_folder = os.path.basename(folder) + '_' + str(number)
        if not os.path.exists(back_folder):
            break
        number = number + 1
    os.mkdir(back_folder)

    # 正则表达式匹配文件扩展名
    pattern = re.compile(r'^(.+)(\.text|\.py)$')
    for folder_name, sub_folder, file_names in os.walk(folder):
        for file_name in file_names:
            if pattern.match(file_name):
                shutil.copy(os.path.join(folder_name, file_name), back_folder)


choose_file('/Users/alex/PycharmProjects/first/radom')
