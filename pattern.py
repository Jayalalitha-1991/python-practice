n= int(input("enter number: "))

class Pattern:
    def tri():

        for i in range(n):
            for j in range(i+1):
                print("aa", end=" ")
                
            print("")
    tri()

    def square():
        for i in range(n):
            for j in range(n):
                print("@", end = "")
            print("")
    square()