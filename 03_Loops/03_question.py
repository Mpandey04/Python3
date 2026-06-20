#Multiplication table printer
#Print thr multiplication table for a given number upto 10,but skip the fifth iteration.

number=int(input("Give number for multiplication\n"))
for i in range(1,11):
    if i==5:
        continue
    print(number,"X",i,"=",(number*i))