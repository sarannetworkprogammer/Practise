class A:


    def __init__(self):
        print("this is inside init A")

    def feature1(self):
        print("this is feature1")

    def feature2(self):

        print("this is feature3")


class B(A):

    def __init__(self):

        print("this is inside B")

    def feature3(self):
        print("this is feature3")

    def feature4(self):
        print("this is holiday")


a1 = B()

a1.feature3()
