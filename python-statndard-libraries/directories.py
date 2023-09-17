"""Directories"""
from pathlib import Path
from time import ctime
path = Path('modules/ecom/shopping/sales.py')
print(ctime(path.stat().st_ctime))
print(path.read_text(encoding='UTF-8'))
print(path.write_text("print('hello')", encoding='UTF-8'))
