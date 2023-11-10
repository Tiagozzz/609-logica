soma = 0

while True:
    numero = int(input('Digite um numero maior que 0 (digite 0 para encerrar): '))
    
    soma = soma + numero

    if numero == 0:
        print(soma)
        break