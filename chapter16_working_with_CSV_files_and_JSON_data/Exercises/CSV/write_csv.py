import csv

# open with 'w', for write a new file
new_file = open('output.csv', 'w', newline='')

# open a writer file
new_file_writer = csv.writer(new_file)

new_file_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
new_file_writer.writerow(['hello, world!', 'eggs', 'bacon', 'ham'])
new_file_writer.writerow([1, 2, 3.14, 4])

new_file.close()