while True:
    nota = int(input('Digite uma nota entre 0 e 10: '))

    if nota >= 0 and nota <= 10:
        print(f'A nota é {nota}')
        break
    else:
        print('Digite uma nota valída')