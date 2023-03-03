'''
Method overloading : different parameters with same method name

Mehod over riding:  different methods with same name in different calss

'''

class Student:



    def __init__(self):

       pass

    def sum(self,a=None, b=None, c=None):

        s = a + b +c

        return s
    def show(self):

        print("sum =",result)



s1 = Student()

if __name__ == "__main__":

    result = s1.sum(5,9,6)
    s1.show()



