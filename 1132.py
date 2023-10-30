# Multiples of 13
x = int(input())
y = int(input())
# any order?
# -> setting max and min.
lower = min(x,y) # obs: it is possible to use lower, higher, lower = max(x, y), min(x, y)
higher = max(x,y)
sum = 0
# to include x and y in the interval, should add +1 to the higher number
for i in range(lower, higher+1):
    if i % 13 != 0:
        sum += i
print(sum)
