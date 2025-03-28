notaLaboratorio = float(input('Digite a nota para o trabalho de laboratório: '))
notaSemestral = float(input('Digite a nota da avaliação semestral: '))
notaExame = float(input('Digite a nota do exame final: '))

if notaLaboratorio >= 0 and notaLaboratorio <= 10 and notaSemestral >= 0 and notaSemestral <= 10 and notaExame >= 0 and notaExame <= 10:
    media = (notaLaboratorio * 2 + notaSemestral * 3 + notaExame * 5) / 10
    if media >= 6:
        print(f'Aprovado com média {media}')
    elif media < 4:
        print(f'Reprovado com média {media}')
    else:
        print(f'Recuperação com média {media}')
else:
    print('Notas inválidas')