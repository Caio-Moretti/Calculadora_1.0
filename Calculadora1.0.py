# Calculadora em Python.
# Loop infinito até selecionar uma opção válida.
while True:
    titulo = " Python Calculator "
    print(titulo.center(50, '='))
    print()
    print('Selecione o número da operação desejada: ')
    print('\n1 - Soma\n'
          '2 - Subtração\n'
          '3 - Multiplicação\n'
          '4 - Divisão\n')
    resp = int(input('Digite sua opção (1/2/3/4): '))  # Variável da resposta.
    n1 = float(input('Digite o primeiro número: '))  # Variável do primeiro número.
    n2 = float(input('Digite o segundo número: '))  # Variável do segundo número.
    # Condicionais para as opções.
    if resp == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        break  # Esse break quebra o looping infinito (o usuário selecionou uma opção válida).
    elif resp == 2:
        print(f'{n1} - {n2} = {n1 - n2}')
        break
    elif resp == 3:
        print(f'{n1} x {n2} = {n1 * n2}')
        break
    elif resp == 4:
        print(f'{n1} ÷ {n2} = {n1 / n2}')
        break

    # Erro caso o usuário digite a opção errada.
    # Mostra o erro e reinicia o loop.
    else:
        print('[ERRO] Opção inválida, tente novamente.')
        print()
