# beecrowd | 1176 | Fibonacci Array
t = int(input())

prev, next = 0, 1

array = [0, 1]

for i in range(0, 61):
    # fibonacci + list
    sum = prev + next
    prev, next = next, sum
    array.append(sum)
    
for i in range(0, t):
    n = int(input())
    print(f'Fib({n}) = {array[n]}')
