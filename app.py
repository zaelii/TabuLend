from flask import Flask, render_template,redirect , request, flash, session 

import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'NLETESTE'

DadosLogin = 'DadosLogin.txt'


class loginProxy:
    def __init__(self,DadosLogin):
        self.DadosLogin = DadosLogin

    def verificarLogin(self,username,password):
        if not os.path.exists(self.DadosLogin):     #verifica se o arquivo dado existe 
            return False
        

        with open(self.DadosLogin, 'r') as f:
            for linha in f:
                if f'Usuario: {username}' in linha and f'Senha: {password}' in linha:
                    
                    return True
        return False
    

@app.route('/')
def home():
    return render_template('telalogin.html')


@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('username')
    senha = request.form.get('password')

    Proxy = loginProxy(DadosLogin)  #cria uma instancia do proxy para verificar o login

    if Proxy.verificarLogin(nome,senha):
        session['username'] = nome  #armazenar o nome do usuario logado
        return redirect('/usuariologado')
    else: 
        flash('USUARIO OU SENHA INVALIDO!')
        return redirect('/') 


@app.route('/usuariologado')
def Usuariologado():
    username = session.get('username') 
    if username:
        return render_template('catalogo.html', username=username, jogos=jogos)  
    else:
        return redirect('/')


@app.route('/register', methods=['POST'])
def register():
    nome = request.form.get('name')
    email = request.form.get('email')
    usuario = request.form.get('username')
    senha = request.form.get('password')

    novoUsuario = usuario(nome,email,usuario,senha)

    novoUsuario.salvar()

    return render_template('telainicial.html')

@app.route('/notificar')

@app.route('/telainicial.html')
def telainicial():
    return render_template('telainicial.html')


@app.route('/recuperarsenha.html')
def recuperarsenha():
    return render_template('recuperarsenha.html')


@app.route('/telalogin.html')
def voltartelainicial():
    return render_template('telalogin.html')


@app.route('/telacadastrar.html')
def telacadastrar():
    return render_template('telacadastrar.html')

# Dados fictícios para os jogos

jogos = [
    {'nome': 'Catan', 'editora': 'Devir', 'preco': 'R$ 25,00', 'status': 'alugado', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\catan.jpg'},
    {'nome': 'Jenga', 'editora': 'Hasbro', 'preco': 'R$ 30,00', 'status': 'disponivel', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\jenga.jpg'},
    {'nome': 'Zombicide', 'editora': 'Galapagos', 'preco': '20,00', 'status': 'disponivel', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\zombicide.jpg'},
    {'nome': 'War', 'editora': 'Grow', 'preco': 'R$ 35,00', 'status': 'alugado', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\war.jpg'},
    {'nome': 'Dixit', 'editora': 'Devir', 'preco': 'R$ 25,00', 'status': 'disponivel', 'dias_aluguel': '7 dias', 'imagem': 'static\imagens\jogos\dixit.jpg'},
]



if __name__ == '__main__':
    if not os.path.exists(DadosLogin):
        with open(DadosLogin, 'w') as f:
            f.write("Cadastro de Usuários:\n")
    app.run(debug=True)
