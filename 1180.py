# beecrowd | 1180 | Lowest Number and Position

# amount of test cases
n = int(input())

values = n(map(int, input().split())) # 1 2 3
array = [int(num) for num in values] # convert each string of the array to int

lowest_number = min(array)
position = array.index(lowest_number)
print(f'Menor valor: {lowest_number}\nPosicao: {position}')
