# Write a program that reads an integer N (1 < N < 1000). 
# This N is the number of output lines printed by this program.
n = int(input())

if 1 < n < 1000:
    j = 1
    for i in range(n):       
        print(f'{(j)**1} {(j)**2} {(j)**3}')
        j += 1
