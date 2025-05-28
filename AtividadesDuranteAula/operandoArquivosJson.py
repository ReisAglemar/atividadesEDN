import json

def lerArquivo():
    with open("arquivo.json", "r") as arquivoJson:
        dados = json.load(arquivoJson)
        print(dados)

def escreverNoArquivo(dados):
   with open("arquivo.json", "w", encoding="utf8") as arquivoJson:
      json.dump(dados, arquivoJson, indent=4, ensure_ascii=False)