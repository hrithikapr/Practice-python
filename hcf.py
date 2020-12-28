a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
min_num = min(a,b)
while min_num > 0:
    if(a % min_num  == 0 and b % min_num == 0):
        break
    min_num -= 1
print(f"HCF of {a}, {b} = {min_num}")

for i in range(1, min_num+1):
    if(a % i == 0 and b % i == 0):
        hcf = i
print(f"HCF of {a}, {b} = {hcf}")