cor = str(input('Digite uma cor do semaforo: ')).strip().lower()

if cor == 'vermelho':
    print('PARE!')
elif cor == 'amarelo':
    print('ATENÇÃO')
elif cor == 'verde':
    print('ACELERA!')
else:
    print('Digite uma cor válida')