lista_notas = []

def valida_opcao():
    while True:
        try:
            op = int(input('>> '))
            if op in range (1,3):
                return op
            else:
                print('\nEntrada inválida.')
        except ValueError:
            print('\nEntrada inválida.')

                

while True:
    print('-----Bem-vindo(a)-----')
    print('[1] Calcular média entre 4 notas')
    print('[2] Sair')
    op = valida_opcao()

    if op == 1:
        nota1 = float(input('Digite o primeiro número: '))    
        nota2 = float(input('Digite o segundo número: '))    
        nota3 = float(input('Digite o terceiro número: '))    
        nota4 = float(input('Digite o quarto número: '))   
        media = (nota1 + nota2 + nota3 + nota4) / 4
        nova_lista = [nota1, nota2, nota3, nota4]   
        lista_notas.extend(nova_lista)
        maior_numero = max(nova_lista)
        menor_numero = min(nova_lista)
        print()
        print(f'A médias das notas = {media}')
        print(f'O maior número = {maior_numero}')
        print(f'O menor número = {menor_numero}')
        print('--------------------')
        print()
        nova_lista.clear()
        
    elif op == 2:
        print()
        print('Encerrando programa . . .')
        break