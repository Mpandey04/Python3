# A function is block of code that perform a specific task whenever is called.In bigger programs where be have large amount of code,it is advisable to create or use existing function that make the program flow organized and neat.

a=9
b=8
gmean=(a*b)**(1/2)
print(gmean)

def calculateGmean(a,b):
    mean=(a*b)**(1/2)
    print(mean)

calculateGmean(9,8)


def isGreater(a,b):
    if(a>b):
        print("First Number is Greater ")
    else:
        print("Second Number is Greater ")

def isLesser(a,b):
    pass


    