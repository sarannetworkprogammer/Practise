'''

In this program we have same methodnames in two different classes passing object of another class as variable in another calss


'''

class PyCharm:

     def execute(self):

        print("this is from class Pycharm")


        print("compiling")
        print("running")


class MyEditor:

    def execute(self):

        print("This is executing from myeditor")
        print("spell check")
        print("convention check")
        print("compiling")
        print("Running")

class Laptop:


    def code(self,ide):

        ide.execute()




if __name__ == "__main__":

    ide = MyEditor()

    print(type(ide))
    lap1 = Laptop()


    lap1.code(ide)