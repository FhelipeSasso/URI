# Write an algorithm to calculate and write the value of S, S being given by:
# S = 1 + 1/2 + 1/3 + … + 1/100
x = 1
for i in range(2, 101):
    # reason for 2, 1/2 add to x
    x += 1/i
print(f'{x:.2f}')
