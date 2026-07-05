
# READING A FILE
# f=open("myfile.txt","r")
# # print(f)
# text=f.read()
# # f.write("welcome")
# print(text)
# f.close()

# #WRITING A FILE
# f=open("myfile.txt","w")
# f.write("Hello world")
# f.close()



with open("myfile.txt","w+") as f:
    f.write("Hey i am inside with")
    
