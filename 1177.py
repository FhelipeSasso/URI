# beecrowd | 1177 | Array Fill II

# Write a program that reads a number T and fill a vector N[1000] 
# with the numbers from 0 to T-1 repeated times, like as the example below.

t = int(input())

if 2 <= t <= 50:
    array = []
    # to ensure that the array will be filled from 0 to t-1
    for i in range(1000):
        array.append(i % t)

    for i in range(1000):
        print(f'N[{i}] = {array[i]}')
