bio="good"
class Grandfather:

    place="cbe"
    def land(self,age):
        print(age)

        print(self.place)
        print(bio)




class Father(Grandfather):

    def house(self):
        print("modern")
        print(bio)


class Son(Father):

    def bike(self):
        print("bmw")














o=Son()
o.land(1)
o.bike()
o.house()