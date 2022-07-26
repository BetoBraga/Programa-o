# importa as libs
import json, requests

# essa linha pega os recursos do link e atribui a variavel
response = requests.get("https://api.********.com.br:5001/api/clientes/GetListaDeProdutos?cnpj=***************&token=**********") # censurado info do cliente
# realiza a conversão do response para um formato acessível ao python
json_data = json.loads(response.text)
to_find = input("Referência:  ")
quantidade = input("Quantidade: ")

for s in range(len(json_data)):
	if json_data[s]["CodigoAmigavel"] == to_find: 
            print("O valor de {} é {}.".format(json_data[s]["CodigoAmigavel"], json_data[s]["PrecoVenda"]))
