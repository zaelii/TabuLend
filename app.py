from flask import Flask, render_template, redirect, request, flash, session
from jogo import Jogo
from usuario import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NLETESTE'

# Dados dos jogos e login
jogos_path = 'catalogoJogos.txt'
dados_login_path = 'DadosLogin.txt'

@app.route('/')
def home():
    return render_template('telalogin.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('username')
    senha = request.form.get('password')

    Proxy = loginProxy(dados_login_path)

    loginValido, tipousuario = Proxy.verificarLogin(nome, senha)

    if loginValido:
        session['username'] = nome
        session['tipo'] = tipousuario
        if tipousuario == 'admin':
            return redirect('/Adminlogado')
        else:
            return redirect('/usuariologado')
    else:
        flash('USUARIO OU SENHA INVALIDO!')
        return redirect('/')

@app.route('/adicionarJogo')
def adicionarjogo():
    return render_template('telaCadastrarJogo.html')

@app.route('/Adminlogado')
def Adminlogado():
    username = session.get('username')
    if username:
        jogos = Jogo.catalogoJogos()
        return render_template('telaadmin.html', username=username, jogos=jogos)
    else:
        return redirect('/')

@app.route('/usuariologado')
def Usuariologado():
    username = session.get('username')
    if username:
        jogos = Jogo.catalogoJogos()
        return render_template('catalogo.html', username=username, jogos=jogos)
    else:
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    nome = request.form.get('name')
    email = request.form.get('email')
    username = request.form.get('username')
    senha = request.form.get('password')

    novoUsuario = Usuario(nome, email, username, senha)
    novoUsuario.salvarConta()

    return render_template('telainicial.html')

@app.route('/registerJogo', methods=['POST'])
def registerJogo():
    titulo = request.form.get('titulo')
    editora = request.form.get('editora')
    preco = request.form.get('valor')
    status = request.form.get('status')

    novoJogo = Jogo(titulo, editora, preco, status)
    novoJogo.salvarJogo()

    return redirect('/Adminlogado')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

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

if __name__ == '__main__':
    if not os.path.exists(dados_login_path):
        with open(dados_login_path, 'w') as f:
            f.write("Cadastro de Usuários:\n")
    app.run(debug=True)
