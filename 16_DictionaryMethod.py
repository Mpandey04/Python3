info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info['DOB'] = 2001
print(info)

# info.update({'age': 20})
# info.update({'DOB': 2001})
# print(info)

# info.clear()
# print(info)

# info.pop('eligible')
# print(info)


# del info['age']
# print(info)

newDictionary = info.copy()

print(newDictionary)