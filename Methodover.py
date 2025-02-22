class Animal:
    def makesoun(self):
        print("Some generic sound")


class Dog(Animal):
    def ma(self):
        print("Bark")


class Cat(Animal):
    def makesound(self):
        print("Meow")


ca = Cat()
ca.makesound()
ca.makesoun()
