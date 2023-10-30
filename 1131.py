# lógica: repetir input("Novo grenal (1-sim 2-nao)") enquanto o input não for 2
# se for 2, printar a quantidade de grenais contados (quantas vezes foi inputado 1)
# contagem de vitorias do inter, gremio, verificar se houve empates, printar quem ganhou mais
gols_int = 0
gols_gre = 0
count_draw = 0
count_choice = 0


while True:
    inter, gre = map(int, input().split())
    count_choice = 1 + count_choice

    if inter > gre:
        gols_int += 1
    elif gre > inter:
        gols_gre += 1
    else:
        count_draw += 1

    choice = input("Novo grenal (1-sim 2-nao)" + "\n")
    if choice != '1':
        break

print(f'{count_choice} grenais\nInter:{gols_int}\nGremio:{gols_gre}\nEmpates:{count_draw}')

if gols_int > gols_gre:
    print("Inter venceu mais")
elif gols_int == gols_gre:
    print("Nao houve vencedor")
elif gols_gre > gols_int:
    print("Gremio venceu mais")
