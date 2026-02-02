birthdays = {'alice': 'apr 2', 'bob': 'dec 12', 'carol': 'mar 4'}

while True:
    print('enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")
    else:
        print("i do not have that name in my database")
        print("what is the birthday?: ")
        bday = input()
        birthdays[name] = bday
        print('database updated')