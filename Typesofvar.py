# class Student:
#     name="afsil"
#
#
# o=Student()
# print(o.name)


# static
# class Student:
#     name="afsil"
#     age=1
#
#
# # o=Student()
# print(Student.name)
# print(Student.age)


# instance
class Student:
    def __init__(self,age):
        self.age=age
        print(age)


o=Student(1)