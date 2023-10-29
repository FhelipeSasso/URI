while True:
    n, m = map(int, input().split())

    if n == m:
        break
    elif n > m:
        print("Decrescente")
    elif n < m:
        print("Crescente")
    