
import requests
class Endereco:
    def __init__(self, CEP, logradouro, complemento, bairro, localidade, UF, estado, regiao, ddd ):
        self.CEP = CEP
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.UF = UF
        self.estado = estado
        self.regiao = regiao
        self.ddd = ddd

    def __str__(self):
        return (f"CEP: {self.CEP}\n"
                f"Logradouro: {self.logradouro}\n"
                f"Complemento: {self.complemento}\n"
                f"Bairro: {self.bairro}\n"
                f"Localidade: {self.localidade}\n"
                f"UF: {self.UF}\n"
                f"estado: {self.estado}\n"
                f"regiao: {self.regiao}\n"
                f"ddd: {self.ddd}")



def consultaCep(cep):
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados = resposta.json()

    if dados.get('erro'):
        print("O CEP informado não foi encontrado.")
    else:
        endereco = Endereco(
            CEP=dados.get('cep'),
            logradouro=dados.get('logradouro'),
            complemento=dados.get('complemento'),
            bairro=dados.get('bairro'),
            localidade=dados.get('localidade'),
            UF=dados.get('uf'),
            estado=dados.get('estado'),  # Pode vir como None
            regiao=dados.get('regiao'),  # Pode vir como None
            ddd=dados.get('ddd')
        )
    return endereco

def main():
    while True:
        cep = input("Digite o CEP, ou 'sair para finalizar a consulta': ")

        try:
            if cep == 'sair':
                print("Saindo")
                break

            if cep.isnumeric() and len(cep) == 8:
                endereco = consultaCep(cep)
                print(endereco)
            else:
                raise Exception("São aceitos apenas 8 números, não use hífen!")

        except Exception as e:
            print(e)
main()