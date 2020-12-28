'''m = int(input("Enter the value of rows: "))
n = int(input("Enter the value of columns: "))

print("Enter Matrix of A")
A = matrix(m, n)
print(A)

print("Enter Matrix of B")
B = matrix(m, n)
print(B)

def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inpt = int(input(f"Enter o[{i}][{j}]: "))
            row.append(inpt)
        o.append(row)
    return o'''

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]


B = [[1,2],
     [4,5],
     [7,8]]


C = [[0,0],
     [0,0],
     [0,0]]

for i in range(0, len(C)):
    for j in range(0, len(C[0])):
        for k in range(0, len(B)):
            C[i][j] += A[i][k] * B[k][j]
for row in C:
    print(row)