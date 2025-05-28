import csv

def lerArquivo():
    with open('arquivo.csv', 'r', encoding="utf8") as arquivoCsv:
        dados = csv.reader(arquivoCsv)
        for linha in dados:
            print(linha)

def escreverNoArquivo(dados):
    with open('arquivo.csv', 'w', encoding="utf8", newline="") as arquivoCsv:
        escrita = csv.writer(arquivoCsv)
        escrita.writerow(dados)