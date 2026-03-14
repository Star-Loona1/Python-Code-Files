class Dog:
    Temperament = 'playful'
    def __init__(self, breed, behaviour):
        self.breed = breed
        self.behaviour = behaviour

b1 = Dog('Dalmation', 'Energetic')
b2 = Dog( 'Maltese dog', 'lively')
print("The breeds are ", b1.Temperament)
print('Breed 1 is called ', b1.breed)
print('Breed 1 is ', b1.behaviour)
print('Breed 2 is called ', b2.breed)
print('Breed 2 is ', b2.behaviour)