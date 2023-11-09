lst = []
v = int(input())
lst.append(v)
for i in range(10):
    v *= 2
    lst.append(v)
    print(f'N[{i}] = {lst[i]}')

# you can separte it in 2 for though, example:

# for i in range(10):
#   print(f'N[{i}] = {lst[i]}')
