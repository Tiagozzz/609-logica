partida = int(input('Digite o numero de partida: '))
f = int(input('Digite o final: '))
pulo = int(input('Digite o de quando o numero pula: '))
fV = f + 1

for i in range(partida, fV, pulo):
    print(i)