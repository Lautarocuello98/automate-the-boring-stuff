# find_mistake.py
# Check spreadsheet rows and find incorrect calculated totals.

import ezsheets

ss = ezsheets.Spreadsheet('ID_AQUI')
sheet = ss[0]

# Start at 2 to skip the header
for row_number in range(2, sheet.rowCount + 1):
    row = sheet.getRow(row_number)

    # Stop if the row is empty
    if row[0] == "":
        break

    try:
        beans_per_jar = int(row[0])
        jars = int(row[1])
        total_beans = int(row[2])
    except ValueError:
        # Skip rows with invalid data
        continue

    correct_total = beans_per_jar * jars

    if correct_total != total_beans:
        print("Error found in row:", row_number)
        print("Row data:", row)
        print("Correct total should be:", correct_total)
        break
