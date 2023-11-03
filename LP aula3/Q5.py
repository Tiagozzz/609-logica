soma = 0

for i in range(1,7):
    notas = float(input(f'Digite a {i} nota: '))
    soma = soma + notas

media = soma / 6

print(f'Sua media é {media}')