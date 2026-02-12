import csv

# open csv
example_file = open('example.csv')
# read csv
example_read = csv.reader(example_file)
# list the lines inside
example_data = list(example_read)
print(example_data[0])
print(example_data[1][1])
print(example_data)