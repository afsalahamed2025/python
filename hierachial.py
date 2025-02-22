class SuperCars:
    def cars(self):
        print("Here are the List of SuperCars : ")


class model1(SuperCars):
    def ferrari(self):

        print("Model Ferrari")


class model2(SuperCars):
    def lambo(self,Lambogini):
        print(Lambogini)


class model3(SuperCars):
    def bugati(self):
        print(input(" enter Model Bugatti"))




obj = model1()
obj.cars()
obj.ferrari()


obj = model2()
obj.cars()
obj.lambo("ghdgddg")