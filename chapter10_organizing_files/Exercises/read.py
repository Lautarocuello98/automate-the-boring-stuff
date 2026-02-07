import zipfile

with zipfile.ZipFile('chapter8_1.zip') as z:
    print(z.namelist())