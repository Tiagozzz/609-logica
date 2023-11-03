palavra = str(input('Digite uma palavra: '))
soma = 0

for letra in palavra:
    if letra in 'aeiou':
        soma = soma + 1

print(f'essa palavra possue {soma} vogais')