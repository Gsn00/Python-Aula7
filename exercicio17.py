nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + (nota3 * 2)) / 4

if media >= 6:
    print(f'Aprovado com média {media}')
else:
    print(f'Reprovado com média {media}')
