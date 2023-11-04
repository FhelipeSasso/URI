# (stop when X=0). For each X, print the sum of five consecutive even numbers from X, 
# including it if X is even.
sum = 0
x = int(input())
for i in range(2, x+1, 2):
    if x == 0:
        break
    else:
        sum += i
print(sum)
# have to finish it