import csv

file_data = open('example.csv')
file_reader = csv.reader(file_data)

# with a loop we cant print all lines
for row in file_reader:
    print(f'Row: {str(file_reader.line_num)} - {row}')