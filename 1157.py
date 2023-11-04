n = int(input())
# range(1) to exclude division by zero, range(n+1) to add up "n" to the range.
for i in range(1, n+1):
    if n % i == 0:
        print(i)
        