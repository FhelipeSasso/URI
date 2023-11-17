# beecrowd | 1181 | Line in Array

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
            sum += array[x][y]
            avg = sum/12

if op == 'S':
    print(sum)
elif op == 'M':
    print(avg)
