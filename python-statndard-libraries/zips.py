"""Working with zip files"""

from pathlib import Path

from zipfile import ZipFile
# with ZipFile('files.zip', 'w') as z:
#     for path in Path('ecommerce').rglob('*.*'):
#         z.write(path)
with ZipFile('files.zip', 'w') as z:
    print(z.namelist())
