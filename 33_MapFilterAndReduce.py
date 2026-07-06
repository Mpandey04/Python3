# #MAP
# def cube(x):
#     return x*x*x

# print(cube(5))

# l=[2,3,4,5,6,7,8]
# # newl=[]
# # for item in l:
# #     newl.append(cube(item))

# # print(newl)

# newl=list(map(cube,l))
# print(newl)

# #FILTER
# def filter_function(a):
#     return a>4
# newFilter=list(filter(filter_function,l))
# print(newFilter)



# #REDUCED
from functools import reduce
numbers=[1,2,3,4,5,6,7,8]


sum=reduce(lambda x,y:x+y,numbers)
print(sum)