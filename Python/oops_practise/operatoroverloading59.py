'''
synthetic sugar
+  it calls __add__() method
- it calls __sub__() method

Magic methods

'''


class Student:

    def __init__(self,m1,m2):

        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):

        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m1
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):

        r1 = self.m1 + self.m2
        r2 = self.m2 + self.m2

        if r1 > r2:
            return True

        else:
            return False









if __name__ == "__main__":

    s1 = Student(58,69)
    s2 = Student(6,)

    s3 = s1 + s2
    print(s3.m1)
    print(s3.m2)


    if s1 > s2 :

        print("s1 will win")


    else:

        print("s2 will win")

