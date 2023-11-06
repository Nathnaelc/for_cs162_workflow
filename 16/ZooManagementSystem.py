class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")


class Lion(Animal):
    def __init__(self, name, weight, age, mane_size):
        super().__init__(name, weight, age)
        self.mane_size = mane_size

    def make_sound(self):
        self.roar()

    def roar(self):
        print(f"{self.name} roars loudly!")


class Shark(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def make_sound(self):
        # Sharks are generally silent, but let's add a fun twist.
        print(f"{self.name} splashes water!")

    def swim(self):
        print(f"{self.name} is swimming!")


class Enclosure:
    def __init__(self, name, temperature_range):
        self.name = name
        self.temperature_range = temperature_range
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to {self.name}.")


class Savannah(Enclosure):
    def __init__(self, name):
        super().__init__(name, (25, 31))
        self.feeding_schedule = "Daily"


class SharkEnclosure(Enclosure):
    def __init__(self, name):
        # Adjusted for more realistic range for sharks
        super().__init__(name, (17, 25))
        self.feeding_schedule = "Weekly"


class Zoo:
    def __init__(self):
        self.enclosures = []
        self.animals = []

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)
        print(f"{enclosure.name} has been added to the zoo.")

    def add_animal(self, animal, enclosure_name):
        # Find the enclosure and add the animal to it
        for enclosure in self.enclosures:
            if enclosure.name == enclosure_name:
                enclosure.add_animal(animal)
                self.animals.append(animal)
                return
        print(f"No enclosure found with the name {enclosure_name}.")

    def feed_all_animals(self, food):
        for animal in self.animals:
            animal.eat(food)

    def make_all_animals_sound(self):
        for animal in self.animals:
            animal.make_sound()


# Example usage:
zoo = Zoo()
savannah = Savannah("Savannah Enclosure")
shark_enclosure = SharkEnclosure("Shark Tank")

lion = Lion("Simba", 150, 5, "Large")
shark = Shark("Jaws", 300, 10)

zoo.add_enclosure(savannah)
zoo.add_enclosure(shark_enclosure)

zoo.add_animal(lion, "Savannah Enclosure")
zoo.add_animal(shark, "Shark Tank")

zoo.feed_all_animals("meat")
zoo.make_all_animals_sound()
