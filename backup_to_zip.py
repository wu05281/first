import zipfile, os

def back_to_zip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)  # make sure folder is absolute
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        #如果要备份 的文件夹是 C:\delicious，ZIP 文件的名称就应该是 delicious_N.zip
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        # 第一个出现的不存在的文件名  用来做文件名
        if not os.path.exists(zip_file_name) :
            break
        number = number+1
    # Create the ZIP file.
    print('Creating %s...' % zip_file_name)
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')
    #
    for folderName, subFolders, fileNames in os.walk(folder):
        print('adding folder to zip file: %s' % folderName)
        for fileName in fileNames:
            new_base = os.path.basename(folder) + '_'
            if fileName.startswith(new_base) and fileName.endswith('.zip'):
                continue  # don't backup the backup ZIP files
            backup_zip.write(os.path.join(folderName, fileName))

    backup_zip.close()
    print('Done.')

back_to_zip('radom')
