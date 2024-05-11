class Animal:
    _eat = 0  # class attribute (공통)

    def __init__(self, food):
        self._mouth_open = True  # instance attribute
        self._food = food  # instance attribute

    def set_name(self, name):  # instance method
        self._name = name  # instance attribute
        print("Name changed to <", name, ">")

    def get_mouth_open(self):  # instance method
        if self.get_eat() <= 0:
            self._mouth_open = True
            print("Mouth is open!")
        else:
            self._mouth_open = False
            print("Mouth is closed.")

    def get_food(self):  # instance method
        return self._food

    def get_eat(self):
        return self._eat

    def set_eat(self, eat):  # instance method
        self._eat = eat
        print("Eat changed to", eat)

    def __eq__(self, other):  # special method (override)
        return self._name == other._name


class Gecko(Animal):
    def __init__(self, food):
        super().__init__(food)  # parent's instance attribute

    def eat(self):
        print("I will eat", self.get_food(), "now!")
        self.set_eat(1)
        self.get_mouth_open()

    def get_mouth_open(self):  # instance method
        super().get_mouth_open()
        print("If eat is less than 0, I open my mouth.")

gecko = Gecko("bugs")

gecko.eat()  # class attribute (공통)

gecko.set_name("Coffee")  # instance method
