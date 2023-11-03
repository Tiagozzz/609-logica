sexo = str(input('Digite seu sexo (M - masculino / F - feminino) : ')).strip().lower()

if len(sexo) == 1:
    if sexo == 'm':
        print('masculino')
    elif sexo == 'f':
        print('feminino')
    else:
        print('sexo inválido')
else:
    print('Digite apenas uma letra')
    