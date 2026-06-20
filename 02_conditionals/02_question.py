#Movie ticket pricing
#Movie ticket are priced based on age:$12 for aadults(18 and above),$8 for children.Everyone a $2 discount on wednesday
day=input("Enter day\n")
age=int(input("Enter age\n"))
price_for_movie_ticket=12 if age>=18 else 8
if day=="wednesday":
    price_for_movie_ticket=price_for_movie_ticket-2;
print("Ticekt price for you is $",price_for_movie_ticket)
