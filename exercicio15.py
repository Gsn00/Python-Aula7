num = int(input('Digite um número com 3 dígitos: '))
a = num // 100
b = num % 10

if a == b:
    print(f'O número {num} é capicua')
else:
    print(f'O número {num} não é capicua')