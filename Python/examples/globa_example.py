'''
scope

Local variable
'''

a = 10

print(id(a))


def something():
    a = 9

    x = globals()['a']
    print(id(x))
    print("infun",a)
    globals()['a'] = 15



something()

print("outside", a)





# Local variable can be accessed via funticon
