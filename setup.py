from distutils.core import setup 
import py2exe 
import sys
sys.setrecursionlimit(4000)

options = {"py2exe":{"bundle_files": 1}}
setup(console=["create_database_info.py"],options=options,zipfile=None)