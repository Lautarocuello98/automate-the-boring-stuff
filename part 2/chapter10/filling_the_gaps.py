from pathlib import Path

# Get folder path from user
print('what folder: ')
p = Path.home() / input().strip()

# Check if the path is a valid directory
if not p.is_dir() or not p.exists():
    print('not a folder')
    exit()

print(f"Choose an option:\n")
print("1. order files quiting gaps")
print("2. insert gaps between files and add new files")

# Get user option
option = input().strip()

# Function to get all files in the folder
def get_files(folder):
    files = []
    for file in folder.iterdir():
        if file.is_file():
            files.append(file)
    return sorted(files)

# Option 1: Order files quitting gaps
if option == '1':
    files = get_files(p)

    # Rename files to remove gaps
    for i, file in enumerate(files, start=1):
        prefix = ''.join(filter(str.isalpha, file.stem))
        new_name = p / f'{prefix}{i}{file.suffix}'
        if file != new_name:
            file.rename(new_name)
    print('Files reordered successfully.')

# Option 2: Insert gaps between files and add new files
elif option == '2':
    files = get_files(p)

    if not files:
        print('No files to insert into.')
        exit()

    # Get number of positions to insert
    position = int(input('Possition to insert: ').strip())

    if position < 1 or position > len(files)+1:
        print('Invalid position')
        exit()

    # get the name
    new_file_name = input('new file name: ').strip()


    # Rename files to create gaps
    for i in range(len(files) - 1, position - 2, -1):
        old_file = files[i]
        new_name = p / f'file{i+2}{old_file.suffix}'
        old_file.rename(new_name)
    
    # Create new file at the specified position
    new_file_path = p / f'{new_file_name}{files[0].suffix}'
    new_file_path.touch()

    print('Gap inserted and new file added successfully.')


else:
    print('invalid option')
