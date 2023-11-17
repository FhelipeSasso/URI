# beecrowd | 1180 | Lowest Number and Position

# for some reason it did pass without satisfying the condition of an array with "n" lenght.

# amount of test cases
n = int(input())

values = list(map(int, input().split())) # 1 2 3
array = [int(num) for num in values] # convert each string of the array to int

lowest_number = min(array)
position = array.index(lowest_number)
print(f'Menor valor: {lowest_number}\nPosicao: {position}')
