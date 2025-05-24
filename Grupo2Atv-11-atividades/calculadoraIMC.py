def apresentaImc(imc):
    print(f"Valor do seu IMC: {imc:.2f}")

def classificaImc(imc):
    if imc <= 18.5:
        print("Atenção! Você está abaixo do peso!")
        apresentaImc(imc)
        return

    if imc <= 24.9:
        print("Parabéns! Você está no peso certo!")
        apresentaImc(imc)
        return

    if imc <= 29.9:
        print("Atenção! Você está em sobrepeso!")
        apresentaImc(imc)
        return

    if imc <= 34.9:
        print("Atenção! Você está em obesidade classe I!")
        apresentaImc(imc)
        return

    if imc <= 39.9:
        print("Atenção! Você está em obesidade classe II!")
        apresentaImc(imc)
        return

    print("Atenção! Você está em obesidade classe I!")
    apresentaImc(imc)
    return

def main():
    peso = input("Informe o seu peso em Kg (Ex: 85.5): ")
    altura = input("Informe sua altura em metros (Ex: 1.65): ")

    try:
        peso = float(peso)
        altura = float(altura)
        imc = (peso / (altura * altura))
        classificaImc(imc)

    except ValueError:
        print("Informe apenas valores numéricos, use o ponto para valores decimais")

if __name__ == "__main__":
    main()