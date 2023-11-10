while True:
    nome = str(input('Digite seu nome: ')).lower().strip()
    
    if len(nome) < 3:
        print('Seu nome precisa ter mais que 3 caracteres')
        continue
    else:
        break
while True:
    idade = int(input('Digite sua idade: '))
    
    if idade < 0 or idade > 150:
        print('Idade precisa ser entre 0 e 150')
        continue
    else:
        break
while True:   
    salario = float(input('Digite seu salário: '))

    if salario <= 0:
        print('Digite um salario maior que 0')
        continue
    else:
        break
while True: 
    sexo = str(input('Digite seu sexo (M ou F): ')).lower().strip()
    
    if sexo not in 'm, f' or len(sexo) != 1:
        print('Sexo invalido')
        continue
    else:
        break
while True:   
    estado_C = str(input('Digite seu estado civil(S, C, V ou D): ')).lower().strip()
    
    if estado_C not in 's, c, v, d' or len(estado_C) != 1:
        print('Estado civíl inválido')
        continue
    else:
        print(f'Seu nome é {nome} você tem {idade} anos, seu salário é {salario} reais, seu sexo é {sexo} e seu estado civíl é {estado_C}')
        break