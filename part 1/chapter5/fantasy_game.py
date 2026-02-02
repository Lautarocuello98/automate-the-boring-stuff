stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

def display_inventory(inventory):
    print('inventory: ')
    item_total = 0
    for item, count in inventory.items():
        print(f"{str(count)} {item}")
        item_total = item_total + count
    print(f"total number of items: {str(item_total)}")

display_inventory(stuff)