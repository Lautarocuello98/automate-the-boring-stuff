import ezsheets

ss = ezsheets.createSpreadsheet('My spreadsheet')
sheet = ss[0]
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'

print(sheet['A1'])

sheet['A2'] = 'Lau'
sheet['B2'] = '28'
sheet['C2'] = 'RoboCop'