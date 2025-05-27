import requests

def consultaCotacao(moeda):
    resposta = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda}-BRL")
    dados = resposta.json()
    chave = f"{moeda}BRL"

    if dados.get('status') == 404:
        print("Erro ao consultar, verifique a moeda informada.")
    else:
        cotacao = dados[chave]
        print(f"Valor atual: R$ {float(cotacao.get('bid')):.2f}\n"
              f"Valor máximo: R$ {float(cotacao.get('high')):.2f}\n"
              f"Valor mínimo: R$ {float(cotacao.get('low')):.2f}\n"
              f"Data Consulta: {cotacao.get('create_date')}\n")


def main():
    while True:
        moeda = input("Escolha o código da moeda para consultar, ou sair para finalizar: ")

        if moeda.lower() == 'sair':
            print("Encerrando...")
            break
        else:
            consultaCotacao(moeda.upper())
main()



