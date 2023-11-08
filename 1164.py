#  For example the number 6 is perfect, because 1+2+3 is equal to 6. 
# Your task is to write a program that read integer numbers and print a message informing 
# if these numbers are perfect or are not perfect.

# n to read the quantity of inputs

n = int(input())

for _ in range(n):
    num = int(input())
    sum = 0
    # checking if it is a perfect number
    for i in range(1, num):
        if num % i == 0:
            sum += i
    # (1, num) to avoid division by zero
    if sum == num:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')
