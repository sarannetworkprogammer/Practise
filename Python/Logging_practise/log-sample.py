import logging
'''
debug
info
warning 
Error
critical
'''

logging.basicConfig(filename ="test.log", level=logging.DEBUG,format='%(asctime)s:%(message)s:%(levelname)s')




class calc:


    def add(self,x,y):
        return x + y

    def sub(self,x,y):

        return x - y

    def multiply(self,x,y):

        return x*y

    def divide(self,x,y):

        return x / y



if __name__ == "__main__":
    num_1 = 20
    num_2 = 10

    result = calc()

    add_result = result.add(num_1,num_2)

    logging.debug(add_result)

    print(add_result)

    sub_result = result.sub(num_1,num_2)

    #logging.warning(sub_result)
    logging.debug(sub_result)

    multiply_result = result.multiply(num_1,num_2)

    #logging.warning(multiply_result)
    logging.debug(multiply_result)

    divide_result = result.divide(num_1,num_2)

    #logging.warning((divide_result))

    logging.debug(divide_result)