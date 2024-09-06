from flask import Flask, render_template

app = Flask(__name__)

# Dados fictícios para os jogos
jogos = [
    {'nome': 'Catan', 'editora': 'Devir', 'preco': 'R$ 25,00', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\catan.jpg'},
    {'nome': 'Jenga', 'editora': 'Hasbro', 'preco': 'R$ 30,00', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\jenga.jpg'},
    {'nome': 'Zombicide', 'editora': 'Galapagos', 'preco': 'R$ 20,00', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\zombicide.jpg'},
    {'nome': 'War', 'editora': 'Grow', 'preco': 'R$ 35,00', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\war.jpg'},
    {'nome': 'Dixit', 'editora': 'Devir', 'preco': 'R$ 25,00', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\dixit.jpg'}
]

@app.route('/')
def index():
    return render_template('index.html', jogos=jogos)

if __name__ == '__main__':
    app.run(debug=True)
