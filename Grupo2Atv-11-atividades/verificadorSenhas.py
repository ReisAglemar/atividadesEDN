def verificaSenha(senha):
    if len(senha) > 7:
        for c in senha:
            if c.isnumeric():
                return True
        print("Sua senha deve ter pelo um caractere numérico")
        return False
    else:
        print("Sua senha deve ter pelo menos 8 caracteres")
        return False

def main():
    while True:
        senha = input("Informe sua senha para verificar se é forte, ou digite 'sair' para sair: ")

        if senha.lower() == "sair":
            print("Programa encerrado!")
            break

        if verificaSenha(senha):
            print("Sua senha é considerada uma senha válida!")
            print(f"Sua senha: {senha}")
            break

main()