# Array Change 1

# Write a program that reads an array N [20]. After, change the first element by the last, 
# the second element by the last but one, etc.., 
# Up to change the 10th to the 11th. print the modified array.

array = []
for i in range(20):
    n = int(input())
    # adds n
    array.append(n)

# slice method
array = array[::-1]
# declared to increment the pos of the array
count = 0

for j in array:
    print(f'N[{count}] = {j}')
    count += 1
