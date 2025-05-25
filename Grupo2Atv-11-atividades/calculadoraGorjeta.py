def mensagemErro(entidade):
    print(f"Erro ao inserir o valor da {entidade}:")
    print("São aceitos apenas valores numéricos, uso o ponto para valores decimais!")


def main():
    valorTotalComanda = input("Informe o valor total da comanda: ")

    try:
        valorTotalTratado = float(valorTotalComanda)
        percentualGorjeta = input("Informe o percentual da gorjeta: ")

        try:
            percentualGorjetaTratado = float(percentualGorjeta)
            valorGorjeta = valorTotalTratado * (percentualGorjetaTratado / 100)
            print(f"O valor da gorjeta deve ser de R$ {valorGorjeta:.2f}")

        except ValueError:
            mensagemErro("gorjeta")

    except ValueError:
        mensagemErro("comanda")

main()