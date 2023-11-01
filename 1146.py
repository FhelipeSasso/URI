# Your program must read an integer X indefinited times (the program must stop when X is equal to zero). 
# For each X print the sequence from 1 to X, with one space between each one of these numbers.
while True:
    x = int(input())
    if x == 0:
        break
    else:
        for i in range(x):
            if i + 1 == x:
                print(i + 1, end = '\n')
            else:
                print(i + 1, end = ' ')
