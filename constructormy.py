# class it:
#
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
#
# o= it('afsal')



# class Tiger:



#
#     def mak(self):
#         print('Tiger Is Danger')
#
# class Birds(Tiger):
#     def nice(self):
#         print("Piece full")
#
# o=Birds()
# o.mak()
# o.nice()

# class Tiger:
#
#     def __init__(self):
#         print('Tiger Is Danger')
#
# class Birds(Tiger):
#     def __init__(self):
#         super().__init__()
#         print("Piece full")
#
# o=Birds()



class Afsal:

    def __init__(self):
        print("Afsal")

class Ahamed(Afsal):
      def __init__(self):
          print('Ahamed')

o=Ahamed()


