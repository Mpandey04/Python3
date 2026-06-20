#validate input
#Keep asking the user for input untill they enter a number between 1 and 10.


while True:
    number=int(input("Enter value b/w 1 and 10:\t"))
    if number>1 and number<=10:
        print("Thanks")
        break
    else:
        print("Invalid number,try again:\t")