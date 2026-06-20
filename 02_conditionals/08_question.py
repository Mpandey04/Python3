#password strength checker
# check if a password is "weak","medium", or "strong".criteria:<6 chars(weak),6-10 chars(medium),>10 chars(strong)

password=input("Enter password\n")
length=len(password)
if length<6:
    print("Password is waek")
elif length>=6 and length<10:
    print("Password is medium")
else:
    print("Password is strong")