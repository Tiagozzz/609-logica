num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"o numero {num1} é o maior")
elif num2 > num1 and num2 > num3:
    print(f"o numero {num2} é o maior")
elif num3 > num2 and num3 > num1:
    print(f"o numero {num3} é o maior")
else:
    print("Os numeros são iguais")