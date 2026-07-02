# a=int(input("Enter First Number\t"))
# b=int(input("Enter second Number\t"))

def average(a=10,b=20): #default Arguments
    print("The average is ",(a+b)/2)
    
average()

#keywords arguments
average(b=20,a=40)


#Required Arguments:

def printFullName(fName="Manish",mName="Kumar",lName="Pandey"):
    print("First Name is:",fName,"\t Middle Name :",mName,"\t Last Name:",lName)


printFullName(mName="Dev")

def sumAverage(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
    
average()
c=sumAverage(50,50)
print("Average is:",c)