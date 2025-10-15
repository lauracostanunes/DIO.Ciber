entrada = input().strip()
tentativas = [item.strip().lower() for item in entrada.split(',')]

falhas_consecutivas = 0

for tentativa in tentativas:
    if tentativa == 'falha':
        falhas_consecutivas += 1
        if falhas_consecutivas >= 3:
            print("Conta Bloqueada")
            break
    else:
        falhas_consecutivas = 0
else:
    print("Acesso Normal")