# logical sequence URI 1144
n = int(input())
x = 1
y = 1
for i in range(n * 2):
    print(f'{x} {x**2 + (i % 2)} {x**3 + (i % 2)}')
    x += (i % 2)
    y += (i + 1)
