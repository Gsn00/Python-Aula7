num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 != num2 or num1 != num3 or num2 != num3:
    if num1 <= num2:
        menor = num1
        if (menor >= num3):
            menor = num3
        print(f'O menor número é {menor}')
    elif num1 >= num2:
        menor = num2
        if (menor >= num3):
            menor = num3
        print(f'O menor número é {menor}')
else:
    print('Os números são iguais')