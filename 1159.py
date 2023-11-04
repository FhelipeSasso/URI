# (stop when X=0). For each X, print the sum of five consecutive even numbers from X, 
# including it if X is even.
while True:
    x = int(input())
    sum = 0
    if x == 0:
        break
    elif x % 2 != 0:
        x += 1  
    # iterates x in two in range 5
    for i in range(5):
        sum += x
        x += 2
    print(f'{sum}')
# done
