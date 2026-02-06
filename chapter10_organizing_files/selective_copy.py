import shutil
import os
from pathlib import Path

# user home directory
p = Path.home()


# user input
source_folder = input('which folder do you want to search?:  ')
destination_folder = input('where do you want to copy the files?:  ')

source_path = p / source_folder
destination_path = p / destination_folder

if not source_path.exists():
    print('Source folder does not exist.')
    exit()

# create destination folder if it doesn't exist
destination_path.mkdir(exist_ok=True)

# extension pattern to search for:
extensions = ('.jpg', '.pdf')

# walk through folders
for folders, subfolders, files in os.walk(source_path):
    for file in files:
        if file.lower().endswith(extensions):
            file_path = Path(folders) / file
            shutil.copy(file_path, destination_path)
            print(f'Copied: {file_path} to {destination_path}')
print('File copy operation completed.')


            