import os
def rename_Files():
    file_list = os.listdir('.') #�г�TestĿ¼�µ������ļ�
    for file_name in file_list:
        if file_name.endswith('txt'):# �ҵ�txt�ļ�
            new_file_name = file_name.translate(None, '0123456789')
            # �����ļ��е�������none��������߶�Ӧǰ��
            # ȥ���ļ������������
            print new_file_name
            os.rename(file_name, new_file_name)
            # os.rename(src, dst)
