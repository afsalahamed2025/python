# oops - object oriented programming system / structure
# real time problem solving
# objects and class
# object - real world entities - likes labtop, chair, person , animals, anythings
# class - collection of objects
# class is a blue print of object
# methods and properties
# car-object
# class - model , desing, engin, speed, millaege
#
# uses oops - code reusable , inheritance , modularity , scalbily
# polymorphism, data abstraction , encapulations

class Animal():
    name="###"
    age="*"
    def show(self): #methods
        print("animal information") # self - used to refer a current instance object
        print(f"Animal Name:{self.name}\n Animal Age:{self.age}")
cat=Animal() # instance object
# # now cat can access all properties of animal class
print(cat.name)
print(cat.age)
cat.name="KiYo"
cat.age=2
# print(cat.name)
# print(cat.age)
dog=Animal()
dog.name="Shishimaru"
dog.age=3
# print(dog.name)
# print(dog.age)
dog.show() # dog.show(dog)
cat.show()# cat.show(cat)
# class constructor method

# class Animal():
#
#     # name="###"
#     # age="*"
#     def _init_(self,name,age): # initializer - class own methods  - class constructor
#         self.Name=name
#         self.Age=age
#         print("Animal Class")
#     def show(self): #methods
#         print("animal information") # self - used to refer a current instance object
#         print(f"Animal Name:{self.Name}\n Animal Age:{self.Age}")
# name=input("enter the animal name")
# age=int(input("enter the age"))
# cat=Animal(name,age) # when i create a instance object that time constructor will call automatically
# # cat.name="kiyo"
# # cat.age=2
# cat.show()

# create a class Shapes - 3 variable - name, color, filled ,1 - method - info()
# 3 child class - square, rectangle , circle - 4 variable , name,color,fi
# lled , area, method - area()