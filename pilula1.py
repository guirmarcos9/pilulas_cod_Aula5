def validarSenha(s):
    if len(s) < 8:
        return "Senha invalida, muito curto"
    
    temNumero = False
    temMaiuscula = False
    
    for c in s:
        if c == ' ':
            return 'Senha Invalida, não pode conter espaço'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
            
    if not temNumero:
        return "Senha invalida, precisa de um num pelo menos"
     
    if not temMaiuscula:
        return "Senha invalida, precisa de uma letra maiuscula pelo menos"
        
#main
senha = input("Digite a senha: ")
r = validarSenha(senha)
print(r)