class Base:

    def add(self,name):

        print(1+1)
        print(name)
class Derived(Base):

    def sub(self):

        print(2-1)

on=Derived()
on.sub()
on.add("abc")

