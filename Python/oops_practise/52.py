'''
Variables declared inside init method is called instance variables
Variables declared inside  class outside init are called static variables

name space class name space instance name space
class variables are also called static variables



'''
class Car:

# class variables

    wheels =4


    def __init__(self):

        # instance variables
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2= Car()

c1.mil = 15

#class variables are also called static variables

Car.wheels = 3

print(c1.com,c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
