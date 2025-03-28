salario = float(input('Digite o salário do trabalhador: '))
prestacao = float(input('Digite o valor da prestação: '))

if prestacao > salario * .2:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')