import os
def rename_Files():
    file_list = os.listdir('.') #列出Test目录下的所有文件
    for file_name in file_list:
        if file_name.endswith('txt'):# 找到txt文件
            new_file_name = file_name.translate(None, '0123456789')
            # 将打开文件中的数字用none输出，后者对应前者
            # 去掉文件名里面的数字
            print new_file_name
            os.rename(file_name, new_file_name)
            # os.rename(src, dst)
