# Write an algorithm to calculate and write the value of S, S being given by:
# S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?
x = 1
y = 2
for i in range(2, 19):
    x += (2 * i - 1) / y
    y *= 2
print(f'{x:.2f}')
