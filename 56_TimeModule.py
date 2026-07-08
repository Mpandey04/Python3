import time
# def usingWhile():
#     i=0
#     while i<50000:
#         i+=1
#         print(i)
# def usingFor():
#     for i in range(50000):
#         print(i)
        
# init=time.time()
# usingWhile()
# t1=time.time()-init
# usingFor()
# print(time.time()-init)
# print(t1)


# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")


t=time.localtime()
formatted_value=time.strftime("%y-%m-%d %H:%M:%S",t)

print(formatted_value)