import csv

new_file = open('example.csv')

# Create a DictReader and manually define the field names.
# Each row will be returned as a dictionary using these keys.
file_reader = csv.DictReader(new_file, ['time', 'name', 'amount'])

# Iterate through each row of the CSV file

for row in file_reader:
    # Access values by dictionary keys instead of column indexes.
    print(f"row {file_reader.line_num} - {row['time']}, {row['name']}: {row['amount']}")

new_file.close()