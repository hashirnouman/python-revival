"""Paths"""
from pathlib import Path

Path(r'C:\Program Files\user')
path = Path('modules/ecom/shopping/sales.py')
print(path.exists())
print(path.is_file())
print(path.parent)
print(Path.home())
