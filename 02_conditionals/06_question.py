#Transportation mode selection
# choose a mode of transportation based on the distance(e.g.,<3 km:walk,3-15km:bike,>15km:car).

distance=int(input("Enter your distance\n"))
if distance <3:
    print("Walk")
elif distance >=3 and distance<15:
    print("Bike")    
else:
    print("Car")