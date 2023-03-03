'''
Method overriding:

same method name in two differnt classes it inherts the properties from the parent if that class doesnt have that method

Example

father son story



'''


class A:


    def show(self):

        print(" in A show ")


class B(A):

    def show(self):

        print(" in B show")


a1 = B()

a1.show()