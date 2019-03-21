class Animal(object):
    species = "Animal"

    def __init__(self, name):
        self.name = name
        self.attribtes = []

    def add_attributes(self, attributes):
        if type(attributes) == list:
            self.attribtes.extend(attributes)
        else:
            self.attribtes.append(attributes)

    def __str__(self):
        return self.name + " is of type " + self.species + " and has attribute: " + str(self.attribtes)


def main():
    a1 = Animal('Rover')
    a1.add_attributes(['runs', 'eats'])
    print(a1)


if __name__ == "__main__":
    main()
