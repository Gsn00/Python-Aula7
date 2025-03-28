salarioFixo = float(input('Digite o salário fixo do vendedor: '))
valorVendas = float(input('Digite o valor das vendas desse vendedor: '))

if valorVendas <= 1500:
    print(f'O salário será {salarioFixo + (valorVendas * .03)}')
else:
    print(f'O salário será {salarioFixo + (valorVendas * .05)}')
