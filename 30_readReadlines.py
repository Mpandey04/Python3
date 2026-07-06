# f=open("myfile.txt","r")
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break
#     m1=int(line.split(',')[0])
#     m2=int(line.split(',')[1])
#     m3=int(line.split(',')[2])
#     print(f"Marks of student {i} in Maths is: {m1} ")
#     print(f"Marks of student {i} in Chemistry is: {m2} ")
#     print(f"Marks of student {i} in Biology is: {m3} ")


f=open("myflie2.txt","w")
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()