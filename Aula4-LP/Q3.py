while True:
    nome = str(input('Digite seu nome: ')).lower().strip()
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salário: '))
    sexo = str(input('Digite seu sexo (M ou F): ')).lower().strip()
    estado_C = str(input('Digite seu estado civil(S, C, V ou D): ')).lower().strip()

    if len(nome) < 3:
        print('Seu nome precisa ter mais que 3 caracteres')
    elif idade < 0 and idade > 150:
        print('Idade precisa ser entre 0 e 150')
    elif sexo != 'm' or sexo != 'f' and len(sexo) > 1:
        print('Sexo invalido')
    elif estado_C not in 's, c, v, d':
        print('Estado civíl inválido')
    else:
        print(f'Seu nome é {nome} você tem {idade} anos, seu salário é {salario} reais, seu sexo é {sexo} e seu estado civíl é {estado_C}')
        break