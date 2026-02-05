tableData = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

def printTable(data):
    # Calculate the maximum width of each column
    colWidths = [0] * len(data)
    for i in range(len(data)):
        for item in data[i]:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)

    # Print the table with right-aligned columns
    for row in range(len(data[0])):
        for col in range(len(data)):
            print(data[col][row].rjust(colWidths[col]), end=' ')
        print()  # Newline after each row 
    
printTable(tableData)