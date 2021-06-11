#!/usr/bin/env python3

import sys
import subprocess

if __name__=="__main__":
    subprocess.check_call([sys.executable, 'src/manage.py', 'runserver'])
