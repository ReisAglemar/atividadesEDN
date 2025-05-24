def verificaBissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True

    return False

def main():
    ano = input("Digite um ano e descubra se ele é bissexto (Ex: 1137): ")

    try:
        ano = int(ano)

        if verificaBissexto(ano):
            print(f"Ano {ano} é bissexto!")
        else:
            print(f"Ano {ano} não é bissexto!")

    except ValueError:
        print("São aceitos apenas números inteiros (Ex: 2022).")

if __name__ == '__main__':
    main()