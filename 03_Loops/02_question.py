#sum of evern numbers
#calculate the sum of even numbers upto a given number n.

sum=0;
number=int(input("Give number for sum\n"))


for num in range(1,number+1):
    if num%2==0:
        sum=sum+num;

print("sum of given even number is:",sum)


