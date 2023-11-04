# Write an algorithm to read a value A and a value N. Print the sum of N numbers from A (inclusive). 
# While N is negative or ZERO, a new N (only N) must be read. All input values are in the same line.

# to make it in the same line, we have to turn it in an array
array = list(map(int, input().split()))

#acessing the first element, which is a
a = array[0]
#acessing the last element, which is n
n = array[-1]
sum = 0

# ignore all values that n <= 0
while n <= 0:
    n = int(input())

for i in range(n):
    sum += a
    a += 1

print(sum)
