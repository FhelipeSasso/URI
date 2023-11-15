# beecrowd | 1179  | Array Fill IV

# kinda hard, got a lot of 15/20% error at first. then this code make through it.

odd_array = []
even_array = []

def output_array(array, string):
    for index, num in enumerate(array):
        print(f'{string}[{index}] = {num}')


for i in range(15):
    x = int(input())
    if x % 2 == 0:
        even_array.append(x)
        # clearing the index and the correspondent number of the array
        if len(even_array)==5:
            output_array(even_array, "par")
            even_array = []
    else:
        odd_array.append(x)
        # clearing the index and the correspondent number of the array
        if len(odd_array)==5:
            output_array(odd_array, "impar")
            odd_array = []

output_array(odd_array, "impar")
output_array(even_array, "par")
