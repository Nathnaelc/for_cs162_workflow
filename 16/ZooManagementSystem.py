class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def eat(self, food):
        pass  # Implement eat behavior for each specific animal

    def makeSound(self):
        pass  # Implement sound behavior for each specific animal


class Enclosure:
    def __init__(self, name, temperature_range):
        self.name = name
        self.temperature_range = temperature_range


class Lion(Animal):
    def __init__(self, name, weight, age, mane):
        super().__init__(name, weight, age)
        self.mane = mane

    def roar(self):
        print(f"{self.name} roars loudly!")

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Shark(Animal):
    def swim(self):
        print(f"{self.name} is swimming!")

    def eat(self, food):
        print(f"{self.name} is eating {food}")


class Savannah(Enclosure):
    def __init__(self, name):
        super().__init__(name, (25, 31))
        self.feeding_schedule = "Daily"

    def addAnimal(self, animal):
        pass  # Implement adding animals to the enclosure


class SharkEnclosure(Enclosure):
    def __init__(self, name):
        super().__init__(name, (17, 18))
        self.feeding_schedule = "Weekly"

    def addShark(self, shark):
        pass  # Implement adding sharks to the enclosure


class Zoo:
    def __init__(self):
        self.enclosures = []
        self.animals = []

    def addEnclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def addAnimal(self, animal):
        self.animals.append(animal)

    def feedAllAnimals(self, food):
        for animal in self.animals:
            animal.eat(food)


# Example usage:
zoo = Zoo()
savannah = Savannah("Savannah Enclosure")
shark_enclosure = SharkEnclosure("Shark Tank")

lion = Lion("Simba", 150, 5, True)
shark = Shark("Jaws", 300, 10)

savannah.addAnimal(lion)
shark_enclosure.addShark(shark)

zoo.addEnclosure(savannah)
zoo.addEnclosure(shark_enclosure)
zoo.addAnimal(lion)
zoo.addAnimal(shark)

zoo.feedAllAnimals("meat")
