c1 = 0
c2 = 0
c3 = 0
c4 = 0
vn = 0
vb = 0
total = 0
tentativa = 0

while True:
    voto = int(input("Votos para os respectivos candidatos:\n1 - José;\n2- João;\n3 - Tomás;\n4 - Mariana;\n5 - Voto Nulo;\n6 - Voto em Branco;\nPara sair do sistema, digite 0.\nVote: "))
    if voto == 0:
        break
    elif voto == 1:
        c1 += 1
        total += 1
    elif voto == 2:
        c2 += 1
        total += 1
    elif voto == 3:
        c3 += 1
        total += 1
    elif voto == 4:
        c4 += 1
        total += 1
    elif voto == 5:
        vn += 1
        total += 1
    elif voto == 6:
        vb += 1
        total += 1
    else:
        tentativa += 1
        if tentativa == 3:
            print("Tentativas de voto excedidas. Programa encerrado por segurança em razão a uma anomalia.")
            break
        print("Número inválido. Tente novamente.")
        continue

    div = print("-------------------------")
    vnTotal = vn / 100 * total
    c1Perc = c1 / total * 100
    c2Perc = c2 / total * 100
    c3Perc = c3 / total * 100
    c4Perc = c4 / total * 100

    print(f'Total de votos de cada candidato:\nCandidato 1: {c1} votos - {c1Perc:.2f}% dos votos\nCandidato 2: {c2} votos - {c2Perc:.2f}% dos votos\nCandidato 3: {c3} votos - {c3Perc:.2f}% dos votos\nCandidato 4: {c4} votos - {c4Perc:.2f}% dos votos')
    print(div)
    print(f'Total de votos nulos: {vn}')
    print(div)
    print(f'Total de votos em branco: {vb}')
    print(div)
    print(f'Porcentagem de votos em branco sobre o total de votos: {vnTotal:.2f}%')