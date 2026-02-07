from pathlib import Path
import sys

# Get folder path from user
print('What folder: ')
p = Path.home() / input().strip()

# Check if the path is a valid directory
if not p.is_dir():
    print('Not a valid folder')
    sys.exit()

prefix = input('File prefix (example: spam): ').strip()

print(f"Choose an option:\n")
print("1. order files quiting gaps")
print("2. insert gaps between files and add new files")

# Get user option
option = input().strip()

def extract_number(file, prefix):
    """Extract numeric part from filename"""
    return int(file.stem.replace(prefix, ''))

# Function to get all files in the folder
def get_files(folder, prefix):
    files = []

    for file in folder.iterdir():
        if file.is_file() and file.stem.startswith(prefix):
            number_part = file.stem.replace(prefix, '')
            if number_part.isdigit():
                files.append(file)

    return sorted(files, key=lambda f: extract_number(f, prefix))

# Option 1: Order files quitting gaps
if option == '1':
    files = get_files(p, prefix)
    if not files:
        print('No matching files found')
        sys.exit()

    # Rename files to remove gaps
    for i, file in enumerate(files, start=1):
        new_name = p / f'{prefix}{i}{file.suffix}'
        if file != new_name:
            file.rename(new_name)
    print('Files reordered successfully.')

# Option 2: Insert gaps between files and add new files
elif option == '2':
    files = get_files(p, prefix)

    if not files:
        print('No matching files found.')
        sys.exit()

    # Get number of positions to insert
    position = int(input('Position to insert: ').strip())

    if position < 1 or position > len(files)+1:
        print('Invalid position')
        sys.exit()  



    # Rename files to create gaps
    for i in range(len(files) - 1, position - 2, -1):
        old_file = files[i]
        new_name = p / f'{prefix}{i+2}{old_file.suffix}'
        old_file.rename(new_name)
    
    # Create new file at the specified position
    new_file = p / f'{prefix}{position}{files[0].suffix}'
    new_file.touch()

    print('Gap inserted and new file added successfully.')

# Invalid option
else:
    print('invalid option')
