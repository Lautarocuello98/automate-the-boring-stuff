def spam():
    global eggs
    eggs = 'spam'
def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)

eggs = '24'
spam()
ham()
print(eggs)