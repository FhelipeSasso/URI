# Write a program that reads an integer N. 
# This N is the number of output lines printed by this program.

n = int(input())
j = 0
for i in range(n):
    print(f'{j+1} {j+2} {j+3} PUM')
    # j += 4 p iterar a cada volta do loop, segundo loop = j+1, mas j = 4, logo j1 = 5
    j+=4
    