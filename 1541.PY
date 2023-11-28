#beecrowd | 1541 | Building Houses
import math

# many test cases
while True:
    n = input()
    # must be a string
    if n == '0':
        break

    a, b, c = n.split()

    # regrinha de 3, se eu sei q 8 - 20%, entao x = 100%, queremos x, certo? -> 20x = 8 * 100 ' x = (8 * 100)/20 '
        
    area = int(a) * int(b) * 100 / int(c)
    side = math.sqrt(area) # convert float to integer
    print(int(side)) 
