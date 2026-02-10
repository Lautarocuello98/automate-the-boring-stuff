import ezsheets

ss = ezsheets.Spreadsheet('1lpT1COLi51SDAItBZIGIS9xLmc7guqLLjaDVGOvfEzk')
sheet = ss[0]

rows = sheet.getRows()

rows[1][0] = 'PUMPKIN'
rows[10][2] = '400'
rows[10][3] = '904'

sheet.updateRows(rows)

print("Updated successfully")
