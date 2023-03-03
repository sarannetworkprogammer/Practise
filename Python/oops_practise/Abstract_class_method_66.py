'''
BAC

What is abstract class, why do we need that

Method which doesnt have body are called abstract methods, class which have that method is called abstract class

By default it doesnt support abstract class , you cannot create object


Decorator --@ talking compiler about it

patterns


'''



from abc import ABC, abstractmethod


class Computer(ABC):



    @ abstractmethod
    def process(self):

        pass

class Laptop(Computer):

    def process(self):
        print("its running")


class Whiteboard:

    def write(self):
        print("its writing")

class Programmer:

    def work(self,com):

        print("solving bugs")
        com.process()



#com = Computer()

com1 = Laptop()

com2 = Whiteboard()

#com.process()

prog1 = Programmer()

prog1.work(com1)


#com2.write()