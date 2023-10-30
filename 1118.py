while True:
    # verifica se a nota é coerente
    n1 = float(input())
    while n1 < 0 or n1 > 10:
        print("nota invalida")
        n1 = float(input())
    # semelhante ao bloco acima
    n2 = float(input())
    while n2 < 0 or n2 > 10:
        print("nota invalida")
        n2 = float(input())

    avg = (n1 + n2)/2
    print(f'media = {avg:.2f}')

    new_op = input("novo calculo (1-sim 2-nao)" + "\n")
    # loop para repetir a pergunta até que a resposta seja (1) - continuar, (2) - parar
    while new_op not in ('1', '2'):
        new_op = input("novo calculo (1-sim 2-nao)" + "\n")
    if new_op == '2':
        break
