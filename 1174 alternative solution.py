# it doenst pass, but it works though.

lst = []

for i in range(5):
    a = float(input())

    if a <= 10:
        lst.append(a)

for i, num in enumerate(lst):
    print(f'A[{i}] = {lst[i]}')
