# this is for polymorphism



class PyCharm:


    def execute(self):
        print("compiling")
        print("running")

class Laptop:

    def code(self,ide):

        ide.execute()


ide = PyCharm()
lap1 = Laptop()

lap1.code(ide)