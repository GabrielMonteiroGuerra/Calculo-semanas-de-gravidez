print("Calculo de meses de gravidez")

semana = int(input('Digite a quantidade de semanas: '))

while (semana < 1 or semana >40):
 semana = int(input('Digite uma quantidade de semanas válida: '))

if (semana >= 1 and semana <= 4):
    print('Você está grávida de 1 mês! Parabéns!')
elif (semana >=5 and semana <= 8):
    print('Você está grávida de 2 meses! Parabéns')
elif (semana >=9 and semana <= 13):
    print('Você está grávida de 3 meses! Parabéns')
elif (semana >=14 and semana <= 17):
    print('Você está grávida de 4 meses! Parabéns')
elif (semana >=18 and semana <= 22):
    print('Você está grávida de 5 meses! Parabéns')
elif (semana >=23 and semana <= 27):
    print('Você está grávida de 6 meses! Parabéns')
elif (semana >=28 and semana <= 31):
    print('Você está grávida de 7 meses! Parabéns')
elif (semana >=32 and semana <= 35):
    print('Você está grávida de 8 meses! Parabéns')
elif (semana >= 36 and semana <= 40):
    print('Você está gravida de 9 meses! Parabéns')