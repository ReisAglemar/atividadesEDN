nomeProduto = "Café"
valorProduto = 68.50
quantidadeAdquirida = 2
total = valorProduto * quantidadeAdquirida


comprovanteCompra = f"""
+------------ COMPROVANTE --------------+
|                                       |
|                                       |
| Produto: {nomeProduto:<29}|
| Valor produto: R$ {valorProduto:<20.2f}|
| Quantidade do produto: {quantidadeAdquirida:<15}|                                      
|                                       |
| Total da compra: R$ {total:<18.2f}|
|                                       |
|     Obrigado pela preferência!        |
|            Volte Sempre               |
|_______________________________________|
"""

print(comprovanteCompra)
