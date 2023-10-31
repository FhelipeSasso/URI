# Write a program to read the type of fuel supplied 
# (coded as follows: 1. Alcohol 2. Gasoline 3. Diesel 4. End). 
# If you enter an invalid code (outside the range of 1 to 4) a new code must be requested. 
# The program will end when the inserted code is the number 4.
alc = 0
gas = 0
dies = 0

while True:
    # repeat until the input reaches 4
    choice = int(input())
    if choice == 1:
        alc += 1
    elif choice == 2:
        gas += 1
    elif choice == 3:
        dies += 1
    elif choice == 4:
        break   

print(f'MUITO OBRIGADO\nAlcool: {alc}\nGasolina: {gas}\nDiesel: {dies}')
