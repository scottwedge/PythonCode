#!/usr/bin/env python
# Filename: backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/home/zhuzhu/shuhuang/code/python_study', '/home/zhuzhu/shuhuang/code/shell_study']
# if you are using windows, use source = [r'C:\Documents', r'D:\Word'] or something like that

# 2. backup must be stored in a main backup directory
target_dir = '/home/zhuzhu/shuhuang/code/'   # remember to change this to what you will be using

# 3. The files are backup into a zip file.
# 4. The name of zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'BACKUP FAILED'
