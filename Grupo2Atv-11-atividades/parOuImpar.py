def informaNumerosInseridos(pares, impares):
    totalPares = len(pares)
    totalImpares = len(impares)
    totalNumeros = totalPares + totalImpares

    print("Você escolheu sair, veja um relatório compilado")
    print(f"\nTotal de números pares: {totalPares}")
    print(f"Total de números impares: {totalImpares}")
    print(f"Total de números inseridos: {totalNumeros}")

def main():
    pares = []
    impares = []
    while True:
        entrada = input("Digite um nuḿero inteiro para verificar se par ou impar, ou digite 'fim' para sair: ")

        if entrada.lower() == 'fim':
            informaNumerosInseridos(pares, impares)
            print("\nPrograma encerrado!")
            break

        try:
            entrada = int(entrada)
            if entrada % 2 == 0:
                pares.append(entrada)
                print(f"{entrada} é par!")
            else:
                impares.append(entrada)
                print(f"{entrada} é impar!")
        except ValueError:
            print("Você deve inserir apenas números inteiros.")

main()