# Given the population and growing rate of 2 cities (A and B), 
# she would like to know how many years would be necessary to the smaller city (always A) 
# to be greater than the larger city (always B) in population
t = int(input())
for i in range(t):
    # get values in a line
    pa, pb, g1, g2 = input().split()
    # convert string to int/float
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)/100 # convert to interval 0.1 - 10.0
    g2 = float(g2)/100 # convert to interval 0.1 - 10.0

    # set years to 0 to count in the loop   
    years = 0
    while True:
        pa += int(pa * g1)
        pb += int(pb * g2)
        years += 1

        if pa > pb or years > 100:
            break
    if years <= 100:
            print(f'{years} anos.')
    else:
            print("Mais de 1 seculo.")
