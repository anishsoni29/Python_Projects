#Unlimited number of arguments using the *args
#This is also known as positional arguments

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(3,4,5,3,4,5,4,5,7,8))

def calculate(n,**kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    #     print(kwargs["add"])
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
    

calculate (2, add=3, multiply=5)


class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Ferrari", model = "488 GTB", colour = "red", seats= 2)
print(my_car.make)
    

#This basically adds n number of arguments

#Tk has a very differnt syntax than python.
#All Tk commands and options were converted into the positional arguments such as args* & kwargs**.
#Lots of optional arguments can be passed using the get method.
#In turtle there is a more box kind of code
#There are three methods : Pack, Place, Grid
#You can't mix up pack and grid together in a program

