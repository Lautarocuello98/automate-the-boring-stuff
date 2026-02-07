import pyinputplus as pyip

print('Welcome to Sandwich Market!!')

# prices
BREAD_PRICE = 1.00
PROTEIN_PRICE = 2.50
CHEESE_PRICE = 0.75
EXTRA_PRICE = 0.50

TOTAL_PRICE = 0.0
ORDER = []

QUANTITY = pyip.inputInt('how many sandwiches do you want?\n', min=1)

if pyip.inputYesNo('do you want bread?\n') == 'yes':
    bread = pyip.inputMenu(
        ['wheat', 'white', 'sourdough'],
        prompt='choose bread:\n',
        numbered=True)
    ORDER.append((f'Bread {bread}', BREAD_PRICE))
    TOTAL_PRICE += BREAD_PRICE

if pyip.inputYesNo('do you want protein?\n') == 'yes':
    protein = pyip.inputMenu(
        ['chicken', 'turkey', 'ham', 'tofu'],
        prompt='choose protein:\n',
        numbered=True)
    ORDER.append((f'Protein {protein}', PROTEIN_PRICE))
    TOTAL_PRICE += PROTEIN_PRICE

if pyip.inputYesNo('do you want cheese?\n') == 'yes':
    cheese = pyip.inputMenu(
        ['provolone', 'american', 'swiss', 'cheddar'],
        prompt='choose cheese:\n',
        numbered=True)
    ORDER.append((f'Cheese {cheese}', CHEESE_PRICE))
    TOTAL_PRICE += CHEESE_PRICE

for extra in ['mayo', 'mustard', 'lettuce', 'tomato']:
    if pyip.inputYesNo(f'do you want add extra {extra}?\n') == 'yes':
        ORDER.append((f'Extra {extra}', EXTRA_PRICE))
        TOTAL_PRICE += EXTRA_PRICE

FINAL_PRICE = TOTAL_PRICE * QUANTITY

print('\nYOUR ORDER SUMMARY:')
for name, price in ORDER:
    print(name.ljust(22, '.') + f'${price:.2f}')

print(f'\nThe total for {QUANTITY} sandwich(es) is: ${FINAL_PRICE:.2f}\n')

