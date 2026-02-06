import os
from pathlib import Path
import send2trash

p = Path.home()

source_folder = input('Which folder do you want to clean up?:  ')

source_path = p / source_folder

if not source_path.exists():
    print('Source folder does not exist.')
    exit()

# Confirm action
confirm = input('This will move all empty files to the trash. Continue? (y/n): ')
if confirm.lower() != 'y':
    print('Operation cancelled.')
    exit()
    
# walk through folders
for folders, subfolders, files in os.walk(source_path):
    for file in files:
        file_path = Path(folders) / file
           
        try:
            if file_path.stat().st_size == 0:
                send2trash.send2trash(file_path)
                print(f'Deleted: {file_path}')
        except Exception as e:
            print(f'Error deleting {file_path}: {e}')
print('Cleanup complete.')
