class student1:
    grade = "B"
    print(grade)

obj = student1()

#second class activity

class student2:
    grade = 'A'
    name = "Jeff"

    def intro(self):
        print("Introduction of the student")

    def detail(self):
        print(self.name)
        print(self.grade)

objec = student2()

objec.intro()
objec.detail()

#third class activity
class Parrot:
    species = "African Grey Parrot"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} {}".format(self.name, song)
    def dance(self):
        pass


object3 = Parrot("Bim", "10")
object4 = Parrot('Jim', '4')

print('My parrots age is {}, its name is {} and its species is the {}'. format(object3.age, object3.name, object3.species))

print(object3.sing("Happy Birthday"))

#4th class activity


