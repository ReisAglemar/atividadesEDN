def calculaMedia(notas):
    media = sum(notas) / len(notas)
    return media

def main():
    notas = []

    while True:
        nota = input("Digite a nota (0 a 10), ou digite 'fim' para calcular a média e sair: ")

        if nota.lower() == "fim" and len(notas) > 0:
            media = calculaMedia(notas)
            print(f"A média da turma é: {media}")
            print(f"Total de notas: {len(notas)}")
            print("Saindo...")
            break

        if nota.lower() == "fim" and len(notas) == 0:
            print("Notas não foram inseridas.")
            print("Saindo...")
            break

        try:
            notafloat = float(nota)
            notas.append(notafloat)
        except ValueError:
            pass

main()
