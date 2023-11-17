# basically, it is the same thing of 1181 URi, the difference between those exercises is using a column instead of a line.

# beecrowd | 1182 | Column in Array

array = []
sum = 0
index = int(input())
# sum or average
op = input()
# fill the array 12x12
for i in range(12):
    line = []
    for j in range(12):
        num = float(input())
        line.append(num)
    array.append(line)
# sum and average 
for x in range(12):
    for y in range(12):
        if x == index:
            # switching the order of y and x you're acessing the line, if you switch x for y you're acessing the column.
            sum += array[y][x]
            # in this case it is not a problem to let the "avg" operation stay inside of the loop.
            avg = sum/12

if op == 'S':
    print(f'{sum:.1f}')
elif op == 'M':
    print(f'{avg:.1f}')
