import operandoArquivosCsv, operandoArquivosTxt, operandoArquivosJson

def solicitopcao():
    operacao = input("Selecione 1 para leitura, ou 2 para escrita: ")
    return operacao

def main():

    csv = operandoArquivosCsv
    txt = operandoArquivosTxt
    json = operandoArquivosJson

    print("Escolha o tipo de arquivo que deseja manipular:")
    print("1 - CSV")
    print("2 - JSON")
    print("3 - TXT")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        operacao = solicitopcao()

        if operacao == "1":
            csv.lerArquivo()
        else:
            dados = input("Insira dados ao arquivo (csv): ")
            csv.escreverNoArquivo(dados.split(","))

    if opcao == "2":
        operacao = solicitopcao()

        if operacao == "1":
            json.lerArquivo()
        else:
            dados = input("Insira dados do arquivo (json), exemplo(chave1:1, chave2:2, ...): ")
            pares = dados.split(",")
            dados = {}

            for par in pares:
                chave, valor = par.split(":")
                dados[chave.strip()] = valor.strip()

            json.escreverNoArquivo(dados)

    if opcao == "3":
        operacao = solicitopcao()

        if operacao == "1":
            txt.lerArquivo()
        else:
            dados = input("Insira dados do arquivo (txt): ")
            txt.escreverNoArquivo(dados)

    else:
        print("Algo não saiu bem... verifique sua entrada.")

if __name__ == "__main__":
    main()