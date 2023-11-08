# A Prime Number is a number that is divisible only by 1 (one) and by itself. For example the number 7 is Prime, 
# because it can be divided only by 1 and by 7.

n = int(input())

for i in range(n):
    num = int(input())

    prime = True
    for j in range(2, num):
        if num % j == 0:
            prime = False
            break
    
    if prime:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
        