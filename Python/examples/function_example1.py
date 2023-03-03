# formal arguments : arguments which are in function definition

# actual arguments :  argument which we pass
#position
#key word







def person(name,age=18):
    print(name)
    print(age)

#person('navin',25)

#if we dont know the sequence key word arguments

person(age =25,name = 'navin')



#variable length arguments


# * multiple values
def sum(a,*b):
    c =a
    for i in b:
        c = c + i
    print("sum=",c)

sum(5,6,7,8,9,10)


