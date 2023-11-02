# logical solution
# Read a value N.
# Calculate and write its corresponding factorial. Factorial of N = N * (N-1) * (N-2) * (N-3) * ... * 1.
n = int(input())
fat = n
if 0 < n < 13:
    for i in range(1, n):
        fat = fat * i
        i -= 1
print(fat)
