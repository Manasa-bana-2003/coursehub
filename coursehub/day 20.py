class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def speak(self):
        pass
    def info(self):
        return f"{self.name} is a {self.species}"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!!"
dog=Dog("buddy","Dog")
cat=Cat("kitty","Cat")
print(dog.info())
print(cat.info())
print(dog.speak())
print(cat.speak())