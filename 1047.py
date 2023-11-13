# Read the start time and end time of a game, in hours and minutes 
# (initial hour, initial minute, final hour, final minute).

start_hour, start_minute, end_hour, end_minute = map(int, input().split())

start_minute += start_hour*60
end_minute += end_hour * 60

time = end_minute - start_minute

if time <= 0:
    time += 24*60

hours = time//60
minutes = time%60

print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')
