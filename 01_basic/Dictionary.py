chai_types={"Masala":"spicy","Ginger":"Zesty","Green":"Mild"}
print(chai_types["Masala"])

print(chai_types)
# for tea in chai_types:
#     # print(tea)
#     print(tea,chai_types[tea])

# for key,values in chai_types.items():
#     print(key,values)


chai_types["Earl Grey"]="citrus"
print(chai_types)

chai_types.pop('Ginger')
print(chai_types)

chai_types.popitem()
print(chai_types)

del chai_types['Green']
print(chai_types)

chai_types_copy=chai_types.copy()

tea_shop={
    "chai":{
        "masala":"tasty",
        "gereen":"Not bad",
        "ginger":"zesty"
    },
    "Tea":{
        "Black":"strong"
    }
}
print(tea_shop['chai'])

squared_num={x:x**2 for x in range(6)}
print(squared_num)

squared_num.clear()

keys=['Masala',"Ginger","Lemon"]
default_value="Dilicious"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)
