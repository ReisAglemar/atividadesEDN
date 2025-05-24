def calculadora(primeiroTermo, segundoTermo, operador):
    if operador == '+':
        resultado = primeiroTermo + segundoTermo
        return f"O resultado da soma é: {resultado:.2f}"

    elif operador == '-':
        resultado = primeiroTermo - segundoTermo
        return f"O resultado da subtração é: {resultado:.2f}"

    elif operador == '*':
        resultado = primeiroTermo * segundoTermo
        return f"O resultado da multiplicação é: {resultado:.2f}"

    elif operador == '/':
        if segundoTermo == 0:
            return "Não é possível dividir por zero"
        else:
            resultado = primeiroTermo / segundoTermo
            return f"O resultado da divisão é: {resultado:.2f}"

    return None

def main():

    while True:
        primeiroTermo = (input("Digite o primeiro termo: "))
        segundoTermo = (input("Digite o segundo termo: "))

        try:
            primeiroTermo = float(primeiroTermo)
            segundoTermo = float(segundoTermo)

            while True:
                operador = (input("Escolha um operador (+ - * /): "))
                operadoresValidos = ["+", "-", "*", "/"]

                if operador in operadoresValidos:
                    resultado = calculadora(primeiroTermo, segundoTermo, operador)
                    print(resultado)
                    break
                else:
                    print("Operador invalido!")
                    print("use '+' para adição")
                    print("use '-' para subtração")
                    print("use '*' para multiplicação")
                    print("use '/' para divisão")
            break

        except ValueError:
            print("São aceitos apenas números, use o ponto para os decimais!")

main()
