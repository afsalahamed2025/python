def show(fun):
    def fir():
        print("first")
        fun()
        print("third")
    return  fir

@show
def add():
    print("hsai")
add()
