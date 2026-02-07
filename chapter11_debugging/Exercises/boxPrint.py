def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")

    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)


sym = input("Enter a symbol (single character): ")
w = int(input("Enter the box width (greater than 2): "))
h = int(input("Enter the box height (greater than 2): "))

try:
    box_print(sym, w, h)
except Exception as err:
    print("An exception occurred: " + str(err))