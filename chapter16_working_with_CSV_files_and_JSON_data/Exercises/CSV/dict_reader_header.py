import csv

# open a file
new_file = open('exampleWithHeader.csv')

# Create a DictReader object
file_reader = csv.DictReader(new_file)

# Iterate through each row of the CSV file
for row in file_reader:
    
    # Each row is a dictionary, so values are accessed by column names.
    print(f"row {file_reader.line_num} - {row['Timestamp']}, {row['Fruit']}: {row['Quantity']}")

new_file.close()