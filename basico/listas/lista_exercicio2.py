lista = []
contador = 0
while True:
    while contador < 5:
        contador += 1
        lista.append(float(input('Digite a nota: ')))
    media = sum(lista) / len(lista)

    if media >= 7:
        print('Aprovado')
        break
    else:
        lista.append(int(input('Informe a nota da prova final: ')))
        media = sum(lista) / len(lista)
        print(f'Sua média final foi {media}')
        if media >= 5:
            print('APROVADO')
        else:
            print('REPROVADO')
        

 