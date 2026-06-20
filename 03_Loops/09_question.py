# list uniqueness checker 
# check if all element in a list are unique.if a duplicate is found,exit the loop and print the duplicate.
# items=["apple","banana","orange","apple","mango"]


items=["apple","banana","orange","apple","mango"]
unique_item=set()
# print(unique_item)

for item in items:
    if item in unique_item:
        print("Duplicate:",item)
        break
    unique_item.add(item)
    
print(unique_item)