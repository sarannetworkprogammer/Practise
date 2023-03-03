'''
generators give you iterators

making function as generator


in data base you have to fetch 1000 records but you have to work one by one value in that case we use generator



yield is key word for generator
'''



def topten():
    n = 1

    while n <= 10:
        sq = n*n

        yield sq
        n=n+1

values  =  topten()

for i in values:

    print(i)