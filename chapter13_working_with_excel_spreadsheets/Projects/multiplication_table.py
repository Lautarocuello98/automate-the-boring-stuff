#! python3
# multiplication_table.py
# Creates an NxN multiplication table in an Excel spreadsheet.

import sys
import openpyxl
from openpyxl.styles import Font


def main():

    # Check that the user provided exactly one command-line argument.
    # The argument should be the size of the multiplication table.
    if len(sys.argv) != 2:
        print("Usage: py multiplication_table.py <Number>")
        sys.exit(1)

    # Try converting the argument to an integer.
    # If conversion fails or the number is less than 1, exit with an error.
    try:
        n = int(sys.argv[1])
        if n < 1:
            raise ValueError
    except ValueError:
        print("The number must be a positive integer.")
        sys.exit(1)

    # Create a new Excel workbook and select the active sheet.
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Multiplication Table"

    # Define a bold font style for headers.
    bold = Font(bold=True)

    # Fill the first row and first column with header numbers (1..n).
    # These serve as the labels for the multiplication table.
    for i in range(1, n + 1):
        sheet.cell(row=1, column=i + 1).value = i
        sheet.cell(row=1, column=i + 1).font = bold

        sheet.cell(row=i + 1, column=1).value = i
        sheet.cell(row=i + 1, column=1).font = bold

    # Fill the inner cells with multiplication results.
    # Each cell is row * column.
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            sheet.cell(row=row + 1, column=col + 1).value = row * col

    # Save the workbook to a file.
    wb.save("MultiplicationTable.xlsx")

    # Print confirmation message.
    print(f"Created MultiplicationTable.xlsx with a {n} x {n} table.")


if __name__ == "__main__":
    main()
