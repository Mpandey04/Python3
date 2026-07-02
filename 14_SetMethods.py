s1={1,2,3,4,5}
s2={3,5,7,8,9}
s4={9,11,12}
s5={1,2}
print(s1.union(s2))
# s1.update(s2)
print(s1)
print(s1,s2)
print(s1.intersection(s2))

s2.intersection_update(s1)
print(s2)

s3=s1.symmetric_difference(s2)
print(s3)

print(s1.isdisjoint(s4))
print(s1.issuperset(s5))