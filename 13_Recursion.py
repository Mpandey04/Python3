num=int(input("Enter any number for factorial\n"))
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    
print(f"Factoral of {num} is:",factorial(num))



# f0=0
# f1=1
# f2=f1+f0
# f(n)=f(n-1)+f(n-2)
def Fibbonacci(num):
    pass