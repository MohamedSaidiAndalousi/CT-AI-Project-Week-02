def checkout(trousers, tshirts, vests):
    total = trousers * 70.5 + tshirts * 20.89 + vests * 100.3
    return total


trousers = int(input("How many trousers have been bought? "))
tshirts = int(input("How many T-shirts have been bought? "))
vests = int(input("How many vests have been bought? "))

total = checkout(trousers, tshirts, vests)

print("Total amount to pay:", total)
