def trataTexto(texto):
    texto = texto.lower()
    caracteresInvalidos = [" ", ".", ",", "?", "!"]
    for caracter in caracteresInvalidos:
        texto = texto.replace(caracter, "")

    return texto

def verificarPalindromo(texto):
    textoTratado = trataTexto(texto)
    textoPalindromo = textoTratado[::-1]

    if textoTratado == textoPalindromo:
        return True

    return False

def main():
    texto = input("Digite um texto ou palavra para verificar se é um palindromo: ")

    if verificarPalindromo(texto):
        print("É um palindromo")
    else:
        print("Não é um palindromo")

main()