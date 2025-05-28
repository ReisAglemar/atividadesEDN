def lerArquivo():
    with open("arquivo.txt", "r") as arquivo:
        dados = arquivo.readlines()
        for linhas in dados:
            print(linhas, end="")

def escreverNoArquivo(dados):
    with open("arquivo.txt", "w") as arquivo:
        arquivo.writelines(dados)