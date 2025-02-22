from abc import ABC,abstractmethod

class Student(ABC):
    def read(self):
        pass

    def write(self):
        pass
class Stu(Student):
    def read(self):
        print("daily reading")
    def write(self):
        print("daily writing")
    def list(self):
        print("daily listening")

o=Stu()
o.write()
o.list()
o.read()




