# class Stu:
#
#     def show(self):
#         print("hai")
#
#     def add(self):
#         print(1 + 1)
#
#
# o = Stu()
# o.show()
#
# o.add()

# class bio:
#     def resume(self, Name, district, age):


     # print("Name:", Name)
     # print("District:", district)
     # print("Age:", age)


# print(input("enter the name"))
# print(input("enter the  district"))
# print(input("enter the  age"))
# o = bio()
# o.resume("Afsal","Coimbatore", "21")

class Bio:
    def resume(self, Name, District, Age):
        print("Name:", Name)
        print("District:", District)
        print("Age:", Age)


name = input("Enter your name: ")
district = input("Enter your district: ")
age = input("Enter your age: ")

o = Bio()
o.resume(name, district, age)
