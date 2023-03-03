'''
Instance methods

class methods

static methods

varibles-2

class&static are same

accessor methods ,mutator methods
just fetch methods

mutator change the values

Getters
setters

Getter fetches the values i.e called accessor methods

Setter changes the values modify the values are called mutator methods


instance methods always argument will be self

class method key word is cls, for class method there is another value , to pass, so we used decorator



'''



class Student:

    school = "Telusko"

# outside the constructor ----init ----------constructor


    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m3
        self.m3 = m3

    def avg(self):

        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1 = value
# decorator
    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is student class in abc moduel")




s1 = Student(34,67,32)
s2 = Student(89,32,12)
s3 = Student(1,2,3)

s1.avg()
print("average",s1.avg())

print(s2.avg())

print(s1.m1,s1.m2,s1.m3)

print(Student.getschool())

Student.info()