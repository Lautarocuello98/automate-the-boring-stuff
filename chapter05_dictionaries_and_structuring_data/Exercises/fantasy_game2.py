
def display_inventory(inventory):
    print('inventory: ')
    item_total = 0
    for item, count in inventory.items():
        print(f"{str(count)} {item}")
        item_total = item_total + count
    print(f"total number of items: {str(item_total)}")



def add_inventory(inventory, addeditems):
    for item in addeditems:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory [item]= 1
    return inventory



inv = {"gold coin": 42, "rope": 1}
dragoon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

inv = add_inventory(inv, dragoon_loot)
display_inventory(inv)