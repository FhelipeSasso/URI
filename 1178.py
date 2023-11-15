# beecrowd | 1178 | Array Fill III

# For each position of the array N print "N[i] = Y", where i is the array position and Y is the number stored in that 
# position. 
# Each number of N[...] must be printed with 4 digits after the decimal point.

x = float(input())
array = []
    
for i in range(100):
    array.append(x)
    x = x/2
    
for i in range(100):
    print(f'N[{i}] = {array[i]:.4f}')
