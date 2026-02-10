# convert_to_other_format.py
# Upload a spreadsheet to Google Sheets, convert it to another format, and download the result locally.

import ezsheets
import os
import sys

# Check that exactly one argument (the file path) was provided
if len(sys.argv) != 2:
    print('Usage: python convert_to_other_format <file>')
    sys.exit(1)

# Get and clean the input file path
input_file = sys.argv[1].strip()

# Validate file path
if not input_file:
    print("Error: empty file path.")
    sys.exit(1)

# Check if the file exists
if not os.path.exists(input_file):
    print("Error: file not found:", input_file)
    sys.exit(1)

# Ensure the path refers to a file and not a directory
if not os.path.isfile(input_file):
    print("Error: not a file:", input_file)
    sys.exit(1)

# Upload the file to Google Sheets (conversion happens here)
print(f'Uploading {input_file}...')
ss = ezsheets.upload(input_file)
print("Upload complete.")

# Ask the user which format to convert to
print("Choose what you want to convert:")
print('1) Excel')
print('2) CSV')
print('3) TSV')
print('4) PDF')
print('5) HTML')

choice = input("Enter option number: ")

# Download the spreadsheet in the selected format
if choice == "1":
    ss.downloadAsExcel()
elif choice == "2":
    ss.downloadAsCSV()
elif choice == "3":
    ss.downloadAsTSV()
elif choice == "4":
    ss.downloadAsPDF()
elif choice == "5":
    ss.downloadAsHTML()
else:
    print("Invalid option")
    sys.exit(1)

print("Conversion finished.")
