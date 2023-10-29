n = int(input())
# setting test cases
for i in range(n):
    x, y = map(int, input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        div = x/y
        print(x/y)