# Read an integer N that is the number of test cases.
# Each test case is a line
# containing two integer numbers X and Y.
# Print the sum of all odd values between them,
# not including X and Y.

while True:
    values = [int(x) for x in input().split()]
    n = max(values)
    m = min(values)

    if m <= 0 or n <= 0:
        break

    inline = ""
    sum = 0

    for i in range(m, n+1):
        sum += i
        inline += str(i) + " "

    print(f'{inline} Sum={sum}')


