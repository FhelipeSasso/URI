# beecrowd | 1151 | Easy Fibonacci
prev, next = 0, 1
sum = 0

x = int(input())
if 0 < x < 46:
    for i in range(0, x):
        if i == x - 1:
            print(sum)
        else:
            # space between each number
            print(sum, end=' ')
        # sequence maker ~ fibonacci
        prev, next = next, sum
        sum = prev + next
