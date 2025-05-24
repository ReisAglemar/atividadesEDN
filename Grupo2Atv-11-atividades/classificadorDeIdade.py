


def classificacao(classificacao):
    print(f"Com base na sua idade, você está classificado como: {classificacao}")


idade = (input("Digite sua idade em números (0 a 120) e veja sua classificação "))

try:
    idade = int(idade)

    if  0 <= idade <= 120:

        if idade <= 12:
            classificacao("Criança")

        elif idade <= 17:
            classificacao("Adolescente")

        elif idade <= 59:
            classificacao("Adulto")
        else:
            classificacao("Idoso")

    else:
        print("Por favor insira uma idade dentro do intervalo permitido (0 e 120)")

except ValueError:
    print("São aceitos apenas números inteiros (0 a 120)")


