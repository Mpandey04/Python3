# Factorial calculator
#compute the factorial of a number using while loop

number_for_factorial=int(input("Give any number for factorial\n"))
factorial=1

while number_for_factorial>0:
    factorial*=number_for_factorial
    number_for_factorial=number_for_factorial-1
print("Factorial:",factorial)