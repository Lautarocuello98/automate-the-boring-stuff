
# text_to_spreadsheet.py
# Reads multiple text files and writes their contents into an Excel spreadsheet.
# Each input file is written to a separate column, and each line becomes a row.

import openpyxl

# Collect file names from the user
filenames = []
while True:
    # Ask for a file name; stop if the user presses Enter
    filename = input('Give me a file (Enter to finish): ').strip()
    
    if filename == '':
        break
    
    filenames.append(filename)

# Exit if no files were provided
if not filenames:
    print('No files provided.')
    exit()

# Create a new Excel workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Text to spreadsheet'

# Process each file and write its contents to a separate column
for col, filename in enumerate(filenames, start=1):
    print(f'Processing: {filename}')

    try:
        # Open the file using UTF-8 encoding to avoid character issues
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Skip files that do not exist
        print(f'File not found: {filename}, skipping.')
        continue

    # Write each line of the file into the spreadsheet
    # Each line becomes a new row in the current column
    for row, line in enumerate(lines, start=1):
        sheet.cell(row=row, column=col).value = line.strip()

# Save the workbook to disk
wb.save('output.xlsx')
print('Done. Spreadsheet saved as output.xlsx')