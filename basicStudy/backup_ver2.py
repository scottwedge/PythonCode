#!/usr/bin/env python
# Filename: backup_ver2.py

import os
import time

# 1. The files and directories to be backed up are specified in a list
source = ['/home/zhuzhu/shuhuang/code/shell_study', '/home/zhuzhu/shuhuang/code/python_study']
# if you are using windows, using source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup dirextory
target_dir = '/home/zhuzhu/shuhuang/code/'   # Remember change this to what you will be using

# 3. The files are backup into a zip file
# 4. The current day is the name of subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# creat the subdirectory if it is't already here
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successful create directory', today

# The name of the zip file
target = today + os.sep + now + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'BACK FAILED'
