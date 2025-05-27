import requests

def verificaIdadePorNome(nome):
    resposta = requests.get(f"https://api.agify.io/?name={nome}")
    return resposta.json()

def main():
    while True:
        nome = input("Informe seu nome, ou digite 'x' para sair: ")

        if nome == 'x':
            print("Obrigado por usar o sistema!")
            break
        else:
            resposta = verificaIdadePorNome(nome)
            print(resposta)
main()