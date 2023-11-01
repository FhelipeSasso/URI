# Write an program that reads two numbers X and Y (X < Y).
# After this, show a sequence of 1 to y, passing to the next line to each X numbers.
x, y = map(int, input().split())
linha = 0
for i in range(y):
    linha += 1
    if linha == x:
        print(i+1, end ='\n')
        linha = 0
    else:
        print(i+1, end = ' ')
