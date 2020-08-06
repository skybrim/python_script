#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@file: find_all_pdf.py
@author: wiley
@datetime: 2020/8/6 1:53 PM

找到所有 pdf
"""

import sys
import shutil
import os
import re
import platform

path = str(sys.argv[1])
slash = '\\' if platform.system() == 'Windows' else '/'
pdf_dir = path + slash + 'pdf' + slash

# 创建 pdf 文件夹
if not os.path.exists(pdf_dir):
    os.mkdir(pdf_dir)

# copy pdf
columns = []
for folder_name, sub_folders, file_names in os.walk(path):
    # create column folder
    if folder_name == path:
        columns = sub_folders
        columns.remove('pdf')
        for column in sub_folders:
            if column == 'pdf':
                continue
            if not os.path.exists(pdf_dir + column):
                os.mkdir(pdf_dir + column)

    # copy pdf
    cur_column = ''
    for column in columns:
        if column in folder_name:
            cur_column = column
    for file_name in file_names:
        if not re.match('.*\.pdf$', file_name):
            continue
        source = folder_name + '/' + file_name
        destination = pdf_dir + cur_column + slash + file_name
        shutil.copy(source, destination)


if __name__ == '__main__':
    pass
