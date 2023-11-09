# read an array A[100]
# print all array positions that store a number less or equal to 10 and the number stored in that position.

lst = []

for i in range(100):
    a = float(input())
    lst.append(a)

    if a <= 10:
        print(f'A[{i}] = {a}')
