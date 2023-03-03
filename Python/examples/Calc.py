'''
if we are using python file as module we dont want other outputs so that we use that


'''

def add():
    print("result 1 is ")
    print(__name__)


def sub():

    print("result 2 is ")

def main():
    print("this is main")
    add()
    sub()

if __name__ == "__main__":
    main()
