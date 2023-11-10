while True:
    nome = str(input('Digite seu nome:')).lower().strip()
    senha = str(input('Digite sua senha:')).lower().strip()

    if len(senha) < 4 or len(senha) > 8:
        print('a senha precisa ter entre 4 e 8 caracteres')
    elif senha == nome:
        print('A senha não pode ser o seu nome')
    else:
        break