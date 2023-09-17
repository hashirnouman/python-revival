"""Paths"""
from pathlib import Path

Path(r'C:\Program Files\user')
path = Path('ecommerce')
print(path.exists())
print(path.is_file())
print(path.parent)
print(Path.home())
print(path.iterdir())
p = [p for p in path.iterdir()]
print(p)
