horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))

if horas >= 0 and horas < 24 and minutos >= 0 and minutos < 60:
    print(f'O horário {horas}:{minutos} é válido')
else:
    print('O horário é inválido')