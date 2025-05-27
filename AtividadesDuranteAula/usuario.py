import requests

class Pessoa:
    def __init__(self, primeiroNome, segundoNome, pais, email):
        self.primeiroNome = primeiroNome
        self.segundoNome = segundoNome
        self.pais = pais
        self.email = email

    def __str__(self):
        return (f"Nome completo: {self.primeiroNome} {self.segundoNome}\n"
                f"Paiś de origem: {self.pais}\n"
                f"E-mail: {self.email}")

def criaUsuario():
    resposta = requests.get("https://randomuser.me/api/")
    dados = resposta.json()
    usuarioJson = dados["results"][0]

    return Pessoa(
        primeiroNome=usuarioJson["name"]["first"],
        segundoNome=usuarioJson["name"]["last"],
        pais=usuarioJson["location"]["country"],
        email=usuarioJson["email"]
    )
def main():
    usuario = criaUsuario()
    print(usuario)

main()