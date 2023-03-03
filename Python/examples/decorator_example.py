def div(a,b):
    print(a/b)


# adding extra features to existing functions

def smart_div(func):


    def inner(a,b):

        if a < b:
            a,b = b,a

        return func(a,b)


div(2,4)