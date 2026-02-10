import openpyxl
from openpyxl.chart import BarChart, Reference

# create a new excel workbook
wb = openpyxl.Workbook()

# get the active worksheet
sheet = wb.active

# write sample data into column A (values 1 to 10)
for i in range(1, 11):
    sheet['A' + str(i)] = i
    
# create a reference to the data for the chart
# this selects cells from A1 to A10
data = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# create a bar chart object
chart = BarChart()

# add the selected data to the chart
chart.add_data(data)

# set the chart title
chart.title = "Sample Bar Chart"

# insert the chart in the worksheet starting at cell C1
sheet.add_chart(chart, 'C1')

# save the workbook to a file
wb.save('chart_example.xlsx')