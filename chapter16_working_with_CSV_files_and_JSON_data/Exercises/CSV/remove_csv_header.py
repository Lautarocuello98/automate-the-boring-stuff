#! python3
# remove_csv_header.py
# Removes the first row (header) from every CSV file in the current directory
# and saves the result into a folder called "headerRemoved".

import csv
import os

# Create output directory if it does not exist
os.makedirs('headerRemoved', exist_ok=True)

# Iterate over every file in the current working directory
for csv_filename in os.listdir('.'):
    # Skip files that are not CSV
    if not csv_filename.endswith('.csv'):
        continue

    print(f'Removing header from {csv_filename}...')

    # Read the CSV file and skip the first row
    csv_rows = []
    csv_file_obj = open(csv_filename)
    reader_obj = csv.reader(csv_file_obj)

    for row in reader_obj:
        # line_num starts at 1, so skip the header row
        if reader_obj.line_num == 1:
            continue
        csv_rows.append(row)

    csv_file_obj.close()

    # Write the remaining rows to a new file in the output folder
    csv_file_obj = open(os.path.join('headerRemoved', csv_filename), 'w', newline='')
    csv_writer = csv.writer(csv_file_obj)

    for row in csv_rows:
        csv_writer.writerow(row)

    csv_file_obj.close()
