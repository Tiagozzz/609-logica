letra = str(input("Digite uma letra: ")).lower().strip()


if len(letra) == 1:
    if letra in "aeiou":
        print("Vogal")
    elif letra in "bcdfghjklmnpqrstvwxz":
        print("consoante")
    else:
        print("caractere invalido")
else:
    print("Digite apenas uma letra")