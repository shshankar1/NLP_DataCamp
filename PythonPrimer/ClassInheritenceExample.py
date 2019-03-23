class Animal(object):
    species = "Animal"

    def __init__(self, name):
        self.name = name
        self.attributes = []

    def add_attributes(self, attributes):
        if type(attributes) == list:
            self.attributes.extend(attributes)
        else:
            self.attributes.append(attributes)

    def __str__(self):
        return self.name + "is of type " + self.species + " and has attributes: " + str(self.attributes)


class Dog(Animal):
    species = "Dog"

    def __init__(self, *args):
        super(Dog, self).__init__(*args)


class Fox(Animal):
    species = "Fox"

    def __init__(self, *args):
        super(Fox, self).__init__(*args)


def main():
    dog = Dog("Rover")
    dog.add_attributes(['lazy', 'beige', 'sleeps', 'eats'])
    print(str(dog))

    fox = Fox("Silver")
    fox.add_attributes(['quick', 'brown', 'run', 'jumps'])
    print(str(fox))


if __name__ == '__main__':
    main()
