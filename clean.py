#!/usr/bin/env python
import shutil
import os


try:
    shutil.rmtree('./static/users')
except:
    pass

try:
    os.remove('./app/data.sqlite')
except:
    pass