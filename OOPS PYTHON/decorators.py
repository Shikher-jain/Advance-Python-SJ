def welcome(fx):
    def mfx(*args, **kwargs):
        print("GM")
        print("kem cho")
        fx(*args, **kwargs)
        print("THANKS")
        print("sayonara")
    return mfx
@welcome
def hello():  #is a fx for welcome function
    print("Hello!!")
@welcome
def add(a,b): #is a fx for welcome function
    print(a+b)
# welcome(hello)()
hello()
welcome(add)(4,4)
add(67,3)