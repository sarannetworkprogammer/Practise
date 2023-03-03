class India:

    def __init__(self):
        print("this is inside Inida init method")

    def capital(self):
        print("New delhi is capital of India")

    def language(self):
        print("Hindi is mostly speaken language")

    def type(self):

        print("India is developing country")

class USA:


    def __init__(self):

        print("this is inside USA CLASS")

    def capital(self):

        print("Washington DC is capital")

    def language(self):

        print("english is mostly spoken")

    def type(self):

        print("USA is well developed country")


obj_ind = India()

obj_usa = USA()

if __name__ == "__main__":
    #obj_usa.capital()
    #obj_usa.type()

    for country in (obj_ind,obj_usa):
        country.capital()
        country.language()
        country.type()