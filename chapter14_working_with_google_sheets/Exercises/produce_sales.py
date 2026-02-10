import ezsheets

# Upload the Excel file and convert it to a Google Sheets spreadsheet
ss = ezsheets.Spreadsheet('1lpT1COLi51SDAItBZIGIS9xLmc7guqLLjaDVGOvfEzk')

# Get the first sheet in the spreadsheet
sheet = ss[0]

# Show row 3 before updating
print("Row 3 BEFORE:", sheet.getRow(3))

# Replace all values in row 3
sheet.updateRow(3, ['Carrots', '2', '20', '=ROUND(B3*C3;2)'])

# Show row 3 after updating
print("Row 3 AFTER:", sheet.getRow(3))

# Get column 1 as a list of values
columnOne = sheet.getColumn(1)

# Convert all values in the column to uppercase
for i, value in enumerate(columnOne):
    columnOne[i] = value.upper()

# Update the entire column in one request
sheet.updateColumn(1, columnOne)

print("Column 1 updated to uppercase.")
print("Spreadsheet URL:", ss.url)