with open('currency.txt') as f:
    lines = f.readlines()

currdict = {}
for line in lines:
    parsed = line.split("\t")
    currdict[parsed[0]] = parsed[1]

amt = int(input("Enter amount: "))
print("Enter the name of currency you want convert this amount to?: ")
print("Available options:\n")
[print(item) for item in currdict.keys()]

currency = input("Please enter one of these: ")
print(f"{amt} INR is equal to {amt*float(currdict[currency])} {currency}")