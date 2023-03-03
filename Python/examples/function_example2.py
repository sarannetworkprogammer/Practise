'''
if we dont how many variables are sending to functions



'''


def person(name, **data):

    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)




person('navin',age = 28,city = 'mumbai',mobile = 9865432)