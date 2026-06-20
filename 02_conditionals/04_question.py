#Fruit ripeness checker
# Determine if a fruit is ripe,overripe,or unripe based on its color.(e.g:Banana:Green-unripe,yellow-ripe,brown-overripe)
Fruit="Banana"
color=input("Give color of your fruit like Green,yellow or brown\n")
if Fruit=="Banana":
    if color=="green":
        print("This fruit is unripe")
    elif color=="yellow":
        print("This fruit is ripe")
    else:
        print("This fruit is overripe")
else:
    print("Invalid Fruit") 