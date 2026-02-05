import os
from pathlib import Path
p = Path.home()

for folders, subfolders, files in os.walk(
    p / 'programacion'/'cs50'
):
    print(f'Current folder: {folders}')
    for subfolder in subfolders:
        print(f'Subfolder of {folders}: {subfolder}')
    for file in files:
        print(f'File inside {folders}: {file}')
    print('')