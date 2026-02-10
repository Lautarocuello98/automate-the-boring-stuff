# spreadsheet_to_text.py
# Reads an Excel spreadsheet and writes the contents into multiple text files.

import openpyxl

# Collect the spreadsheet from the user
filename = input('Enter the spreadsheet name: ').strip()

# Exit if no file was provided
if not filename:
    print('No file provided')
    exit()

print(f'Opening {filename}...')

# Load workbook
try:
    wb = openpyxl.load_workbook(filename)
except FileNotFoundError:
    print(f'File not found: {filename}')
    exit()

sheet = wb.active
filenames = []

# Iterate over columns and write each one to a text file
for col in range(1, sheet.max_column + 1):
    
    output_filename = f'column_{col}.txt'
    print(f'Writing {output_filename}...')
    filenames.append(output_filename)

    with open(output_filename, 'w', encoding='utf-8') as f:

        for row in range(1, sheet.max_row + 1):
            value = sheet.cell(row=row, column=col).value

            if value is None:
                continue

            f.write(f'{value}\n')

print("Done")
print(f'The files are {filenames}')