num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 == num2 and num1 == num3:
    print('Triângulo equilátero')
elif num1 != num2 and (num1 != num3 and num2 != num3):
    print('Triângulo escaleno')
else:
    print('Triângulo Isósceles')