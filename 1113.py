while True:
    n, m = map(int, input().split())

    if n > m:
        print("Decrescente")
    elif n < m:
        print("Crescente")
    else:
        break