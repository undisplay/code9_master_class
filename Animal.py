

class Animal:
        
    foots = 0
    hands = 0
    name = ""
    age = 0

    def __init__(self, foots, hands, name, age):
        self.foots = foots
        self.hands = hands
        self.name = name
        self.age = age

    def display(self):
        print(f"foots:{self.foots},hands:{self.hands},name:{self.name},age:{self.age}")


class Hen(Animal):
    wings = 0
    def __init__(self, foots, wings, name, age):
        super().__init__(foots,0, name, age)
        self.wings = wings

    def display(self):
        print(f"foots:{self.foots},wings:{self.wings},name:{self.name},age:{self.age}")


h1 = Animal(2,2,"Djine",20)
h1.display()


h2 = Animal(2,2,"Freedy",23)
h2.display()

ch = Hen(2,2,"chiken",1)
ch.display()