from datetime import date
from verificadorAnoBissexto import verificaBissexto

def contadorDias(anoNascimento):
    anosBissexto = []
    idadeEmDias = 0
    anoAtual = date.today().year

    for i in range (anoNascimento, anoAtual+1):
        if verificaBissexto(i):
            idadeEmDias += 366
            anosBissexto.append(i)
        else:
            idadeEmDias += 365

    return idadeEmDias, anosBissexto

def main():
    while True:
        anoNascimento = input("Digite o ano de nascimento, ou 'fim' para sair: ")

        if anoNascimento == "fim":
            print("Programa encerrado!")
            break

        try:
            anoNascimento = int(anoNascimento)
            if anoNascimento >= 0:
                idadeEmDias, anosBissextos = contadorDias(anoNascimento)
                print(f"Sua idade em dias é {idadeEmDias} dias.")
                print(f"Os seguintes foram bissextos: {anosBissextos}")
            else:
                print("Você nã pode inserir números menores que zero")

        except ValueError:
            print("Ao informar o ano são aceitos apenas números inteiros")

main()