catnames = []

while True:
    print(f"Enter the name of cat {len(catnames) + 1} (or enter nothing to stop):")
    name = input()
    if name == "":
        break
    catnames = catnames + [name]  # Concatenate to create a new list

print("The cat names are:")
for name in catnames:
    print(" " + name)
