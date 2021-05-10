eggs = 'global'

def spam():
    

    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)


bacon()
print(eggs)
