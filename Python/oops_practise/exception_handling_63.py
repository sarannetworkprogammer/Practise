'''
Errors

compile time : syntax error,

logical error: code is working , for example 2+2 = 1  thats  the error, not correct error

Runtime error

eg divide by zero , its not working for specifi input given by user

Mostly easiest compile error, logical error can also developer findout by unit testing

corner scenarios: what mistakes user can do

Banking software , your software should notstop , your execution should not stop

Normal & critical statement

your execution should not stop at any point of time
if logic raises error basically for critical statements we use

if logic works print try block otherwise except block

except block only execute when you open a resource close it before leaving from there

for example you are opening fridge and close simlarly when you open database connection close it and when you open a
file close it



'''

a = 5

b = 2
try:

    print("resource open")
    print(a/b)
    k = int(input("enter number"))
    print(k)


# except block will be executed if we get error
except ZeroDivisionError as e:

    print("Hey you cannot divide an number by zero ", e)

except ValueError as e:

    print("invalid input",e)


except Exception as e:

    print("something went wrong")

finally:

    print("resource closed")

print("bye")














