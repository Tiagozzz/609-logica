numero = int(input("Digite um número: "))

if numero > 4:
    print("é maior que 4")
elif numero < 4:
    print("é menor que 4")
else:
    print("é igual a 4")



#FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UM NÚMERO INTEIRO E MOSTRA NA TELA SE ESSE NÚMERO DIGITADO É POSITIVO, NEGATIVO OU NEUTRO

numero = int(input("Digite um número: "))

if numero > 0:
    print(f"O {numero} é positivo")
elif numero < 0:
    print(f"O {numero} é negativo")
else:
    print(f"O {numero} é neutro")



#FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR O A ANO QUE ELE NASCEU, E MOSTRE NA TELA SE ELE É MAIOR OU MENOR DE IDADE


ano = int(input("Digite o ano que você nasceu: "))


if ano <= 2005:
    print("é maior de idade")
else:
    print("é menor de idade")


#VERSÃO 2:
ano = int(input("Digite o ano que você nasceu: "))

idade = 2023 - ano

if idade >= 18:
    print(f"Você tem {idade} anos, então é maior de idade")
else:
    print(f"Você tem {idade} anos, então é menor de idade")


#VERSÃO AVANÇADA APENAS PARA DEIXAR REGISTRADO:

import datetime

ano = int(input("Digite o ano que você nasceu: "))

ano_atual = datetime.datetime.now().year

idade = ano_atual - ano

if idade >= 18:
    print(f"Você tem {idade} anos, então é maior de idade")
else:
    print(f"Você tem {idade} anos, então é menor de idade")



#FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UM NÚMERO INTEIRO E POSITIVO E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")
    



numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))


if numero1 > numero2 and numero1 > numero3:
    print(f"O {numero1} é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O {numero2} é o maior")
elif numero3 > numero2 and numero3 > numero1:
    print(f"O {numero3} é o maior")
else:
    print("Os números são iguais")


letra = str(input("Digite uma letra: "))

if letra == "a" or letra == "b":
    print("Qualquer coisa")




semaforo = str(input("Digite uma cor do sinal de trânsito: "))

if semaforo == 'vermelho':
    print("Pare")
elif semaforo == "amarelo":
    print("Atenção")
elif semaforo == "verde":
    print("Siga")
else:
    print("Inválido")


semaforo = str(input("Digite uma cor do sinal de trânsito: "))

match semaforo:
    case "vermelho":
        print("Pare")
    case "amarelo":
        print("Atenção")
    case "verde":
        print("Siga")
    case _:
        print("Inválido")



#QUESTÃO 1:
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O {numero1} é maior que o {numero2}")
elif numero2 > numero1:
    print(f"O {numero2} é maior que o {numero1}")
else:
    print("Os números são iguais")


#QUESTÃO 2:
valor = int(input("Digite um valor: "))

if valor > 0:
    print(f"O {valor} é positivo")
elif valor < 0:
    print(f"O {valor} é negativo")
else:
    print(f"O {valor} é neutro")


#QUESTÃO 3:
sexo = str(input("""
Digite o seu sexo: 
F - Feminino
M - Masculino
""")).upper().strip()

if sexo == 'F' or sexo == 'FEMININO':
    print("F - Feminino")
elif sexo == "M" or sexo == 'MASCULINO':
    print("M - Masculino")
else:
    print("Alternativa inválida")