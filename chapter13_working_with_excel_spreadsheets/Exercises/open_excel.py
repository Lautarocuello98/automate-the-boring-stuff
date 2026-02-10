import openpyxl
print()

wb = openpyxl.load_workbook('example.xlsx')
print(wb.sheetnames)

print()

sheet = wb['Sheet3']
print(sheet)

print()

print(type(sheet))

print()

print(sheet.title)

print()

anotherSheet = wb.active
print(anotherSheet)