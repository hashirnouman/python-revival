"""Working with zip files"""

from pathlib import Path

from zipfile import ZipFile
# with ZipFile('files.zip', 'w') as z:
#     for path in Path('oop').rglob('*.*'):
#         z.write(path)

with ZipFile('files.zip') as z:
    print(z.namelist())
    info = z.getinfo('oop/abstract_class.py')
    print(info.file_size)
    print(info.compress_size)
    z.extractall('extract')
