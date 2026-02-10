import ezsheets

# Create two spreadsheets
ss1 = ezsheets.createSpreadsheet('First Spreadsheet')
ss2 = ezsheets.createSpreadsheet('Second Spreadsheet')

# Get the first sheet from ss1
sheet1 = ss1[0]

# Write some data in ss1
sheet1.updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])

# Copy the first sheet from ss1 to ss2
sheet1.copyTo(ss2)

print("Sheet copied successfully.")
print("First spreadsheet:", ss1.url)
print("Second spreadsheet:", ss2.url)