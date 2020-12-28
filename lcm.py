a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter second number: "))
maxnum  = max(a,b,c)
while(True):
    if (maxnum % a == 0 and maxnum % b ==0 and maxnum % c ==0):
        break
    maxnum += 1
print(f"The LCM of {a}, {b}, {c} = {maxnum}")