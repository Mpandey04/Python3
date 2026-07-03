# try:
#     a = int(input("Enter the number:"))
#     print(f"Multiplication table of {a} is:")

#     for i in range(1, 11):
#         print(f"{a} X {i} = {a*i}")

# except ValueError:
#     print("Please enter a valid integer.")

# except Exception as e:
#     print(e)

# print("some lines of important code")
# print("End of Program")


try:
    num = int(input("Enter the number:"))
    a=[6,7]
    print(a[num])
except IndexError:
    print("Index is out of range")
    