# Read an array X[10]. After, replace every null or negative number of X ​by 1. Print all numbers stored in the array X.
x = []

for i in range(10):
    num = int(input())
    if num <= 0:
        num = 1
        x.append(num)
    else:
        x.append(num)

for i in range(10):
    print(f'X[{i}] = {x[i]}')
