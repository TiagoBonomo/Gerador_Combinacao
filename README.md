![Logo do projeto](/readme_images/logo_projeto.png)

# Gerador de Combinações

Estudo de Desenvolvimento de API utilisando Python/Flask.
A API tem em teoria capacidade de gerar a quantidade de um pouco mais de 3 milhões de combinações, com a quantidade de 15 dezenas cada combinação,
a mesma pode gerar combinações com menos ou mais de 15 dezenas, o range utilizado na geração das combinações e de 1 a 25.
API foi desenvolvida para gerar combinações para para a loteria LOTOFACIL. 

### 📋 Pré-requisitos

* Python 3.9.12
* Flask 2.1.2 

### 🔧 Instalação

Com o Python 3.9.12 ou superior instalado acesse a pasta do projeto onde se encontra o arquivo requirements.txt execute:
	
pip install -r requirements.txt

Após a instalação das dependencias execute:
	
python main.py

## ⚙️ Executando os testes

Para realizar a request deve ser enviado 
dois paramantros, q_combinacoes e q_dezenas.

q_combinacoes -> Quantidade de combinações desejadas.

q_dezenas -> Quantidade de dezenas desejada para cada 
combinação.

Exemplo:

http://localhost:5000/?q_combinacoes=3&q_dezenas=15

![Exemplo execução local 01](/readme_images/print01.png)

Neste exemplo é feita uma requisição de 4 combinações 
contendo 16 dezenas cada combinação,
a resposta é enviada em formato Json

![Exemplo execução local 02](/readme_images/print02.png)

Para realizar request via web segue link abaixo:

Obs: Adicione os valores de parametros como no exemplo abaixo.

Ex: https://apilotofacil.herokuapp.com/?q_combinacoes=10&q_dezenas=15 

![Exemplo execução heroku](/readme_images/heroku001.png)

![Exemplo execução heroku](/readme_images/heroku002.png)

## Links
			
https://apilotofacil.herokuapp.com


## 🛠️ Construído com

* [Python](https://docs.python.org/3/) - Linguagem de Programação Python
* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Framework de Desenvolvimento Web Python
* [request]
* [jsonify]

## 🖇️ Colaborando

* tiagofbonomo@gmail.com

## 📄 Licença

https://choosealicense.com/licenses/mit/

## 🎁 Expressões de gratidão

* Ao TODO que me deu a oportunidade de aprender e compartilhar.
* https://www.youtube.com/watch?v=WWVEymSt1iI
* https://gist.github.com/lohhans/f8da0b147550df3f96914d3797e9fb89
* Obrigado a Todos.
