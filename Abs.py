from abc import ABC,abstractmethod

class Student(ABC):
    def read(self):
       pass

    def write(self):
        pass

class  Stu(Student):
    def read(self):
        print("reading")

    def write(self):
        print("writing")

    def listen(self):
        print("listening")

o=Stu()
o.write()
o.listen()
o.read()