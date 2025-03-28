num = int(input('Digite um número entre 1 e 999: '))

if num > 0 and num < 1000:
    a = num // 100
    b = (num % 100) // 10
    c = (num % 10)
    print(f'Numeros {a}+{b}+{c} é {a+b+c}')
else:
    print('Número inválido')