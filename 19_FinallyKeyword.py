try:
    l=[1,2,4,6,7]
    i=int(input("Enter the index:"))
    print(l[i])

except:
    print("Some error occurred")

finally:
    print("Finally block code will always executed")
    
def func1():
    try:
        s1={1,2,3,4,5,6}
        print(s1)
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("This line of block code will always executed")