# Write a program that reads two integer numbers X and Y. 
# Print all numbers between X and Y which dividing it by 5 the rest is equal to 2 or equal to 3.
x = int(input())
y = int(input())
lower, higher = min(x, y), max(x, y)
# always in ascending order
for i in range(lower+1, higher):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
