# beecrowd | 1564 | Brazil World Cup
# to solve this question, you should use try/except to treat errors

while True:
    try:
        n = int(input())
        if n == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break
