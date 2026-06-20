#Grade calculator
#Assign a letter grade based on a student's score: a(90-100),B(80-89),c(70-79),f(below 60)
marks=int(input("Enter your marks\n"))
if marks>100:
    print("Invalid Grade score")
    exit()
elif marks>=90 and marks <=100:
    print("Your Grade is: A",)
elif marks>=80 and marks<90:
    print("Your Grade is: B")
elif marks>=70 and marks<80:
    print("Your Grade is: C")
elif marks>=60 and marks<70:
    print("Your Grade is: D")
else:
    print("F")