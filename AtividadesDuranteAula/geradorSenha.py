import random
import string

def geradorSenha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():

    while True:
        tamanho = input("Informe o tamanho da sua senha: ")

        try:
            tamanho = int(tamanho)

            if tamanho >= 5:
                senha = geradorSenha(tamanho)
                print(senha)
                break
            else:
                raise Exception("A senha deve ter no mínimo 5 caracteres")

        except ValueError:
            print("São apenas valores numéricos")
            continue

        except Exception as e:
            print(e)
            continue
main()