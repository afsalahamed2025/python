def show(fun):
    def funy():
        print("afsal")
        fun()
        print("ahamed")
    return funy

@show
def add():
    print("hi")
add()

