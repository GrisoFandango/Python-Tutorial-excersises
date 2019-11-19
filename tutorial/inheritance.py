class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
# f = Fish()
# m.eat()
# print(m.age)
# print(isinstance(m, object))
# 0 = object()
# print(issubclass(m, Animal))
print(m.age)
print(m.weight)
