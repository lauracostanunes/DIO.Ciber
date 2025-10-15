def verificar_comando(comando):
    caracteres_suspeitos = [';', '&', '|', '$']
    
    for caractere in caracteres_suspeitos:
        if caractere in comando:
            return "Comando Suspeito"
    
    return "Comando Seguro"

comando_usuario = input()
print(verificar_comando(comando_usuario))