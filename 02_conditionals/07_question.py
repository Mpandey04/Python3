#coffee customization
#customize a coffee order:"small","medium" or "large" with an option for "Extra shot" of espresso.

order_size="medium"
extra_shot=True

if extra_shot:
    coffee=order_size+" coffee with an extra shot"
else:
    coffee=order_size+" coffee"
    
print("Order:",coffee)