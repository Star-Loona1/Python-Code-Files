class parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age
Woo = parrot('Chipster', 5)
Blu = parrot('Blu', 7)
print(Woo.name, ' is a ', Woo.species)
print(Woo.name, ' is ', Woo.age)
print(Blu.name, ' is also a ', Blu.species)
print(Blu.name, ' is ', Blu.age)