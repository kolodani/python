price = 100 # Global variable

def increment():
    price = 200 # Local variable
    result = price + 20
    print(result)
    return result

print(price)
price_2 = increment()
print(price_2)