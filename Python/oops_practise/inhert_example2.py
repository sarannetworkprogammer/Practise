

class A:

    def __init(self):

        print("this is inside A")

    def feature1(self):

        print("this is feature1")

    def feature2(self):

        print("this is feature2")

class B:

    def __init__(self):

        print("this is b")

    def feature3(self):

        print("hello world")


class C(A,B):

    def __init__(self):

        print("inside C")

    def feature4(self):

        print("feature6 inc ")




if __name__ == "__main__":
    c1 = C()
    c1.feature2()