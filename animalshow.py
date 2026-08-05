from abc import ABC, abstractmethod
class animal(ABC):

    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print('Name: {} | Habitat: {}'.format(self.name, self.habitat))

    @abstractmethod
    def speak(self):
        pass


class dog(animal):

    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase

    def speak(self):
        print(f'{self.name} says: {self.phrase}')


d = dog('bob', 'house', 'woof')
d.speak()
d.display()



        