'''
like special variable there is special method __name__
te
special method __init__ Underscores are common





'''


class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


        print("inside init")


    def config(self):
        print("config is ", self.cpu,self.ram)

com1 = Computer("i5", 16)
com2 = Computer("Ryzen 3",8)

com1.config()
com2.config()