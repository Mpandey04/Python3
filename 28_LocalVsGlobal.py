x=4
print(x)
def my_function():
    # global x
    x=10
    print(" Manish")
    print(f"The local x is {x}")

my_function()
print(f"The global x is {x}")