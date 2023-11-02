# ages 
# Write an algorithm to read an undeterminated number of data, each containing an individual's age.
# Calculate and print the average age of this group of individuals.
# The input will be stop when a negative value is read.
# The average should be printed with two digits after the decimal point.
sum = 0
avg = 0
count = 0
while True:
    age = int(input())
    count += 1
    if age < 0:
        break
    else:
        sum += age
        avg = sum/count
print(f'{avg:.2f}')
