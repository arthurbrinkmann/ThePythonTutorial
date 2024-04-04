# Define refill function
def refill(x, y, z):
    return x + y + z

# Define variables
coffee = 10
cream = 5
sugar = 3
caffeination = 0
enough = 100
sip = 5

mug = refill(coffee, cream, sugar)

while caffeination < enough:
    caffeination += sip
    mug -= sip
    if mug == 0:
        mug = refill(coffee, cream, sugar)

print("python does java")
