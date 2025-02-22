a = 100
b = 45
class Globa:
    def add(self):
        print(a + b)
Globa
class Glo(Globa):
    def show(self):
        print(a * b)

class Glor(Glo):
    def test(self):
        print(a/b)


o=Glor()
o.add()
o.show()
o.test()



