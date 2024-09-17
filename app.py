from flask import Flask, render_template, redirect, request, flash, session, url_for
from werkzeug.utils import secure_filename
from jogo import *
from usuario import *
import os

# Dados dos jogos,login e imagens
jogos_path = 'catalogoJogos.txt'
dados_login_path = 'DadosLogin.txt'
imagens_jogos_path = 'static/imagens/jogos'

extensions = {'png', 'jpg', 'jpeg', 'gif'}

def extensaovalida(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NLETESTE'
app.config['UPLOAD_FOLDER'] = imagens_jogos_path


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
        jogos = JogoDeTabuleiro.catalogoJogos()
        return render_template('telaadmin.html', username=username, jogos=jogos)
    else:
        return redirect('/')

@app.route('/usuariologado')
def Usuariologado():
    username = session.get('username')
    if username:
        jogos = JogoDeTabuleiro.catalogoJogos()
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
    
    imagem = request.files['imagem']

    if imagem and extensaovalida(imagem.filename):
        filename = secure_filename(imagem.filename)
        imagem.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        novoJogo = JogoDeTabuleiro(titulo, editora, preco, status, caminho_imagem)
        novoJogo.salvarJogo()

        return redirect('/Adminlogado')

    flash('Tipo de arquivo de imagem não permitido.')
    return redirect(request.url)
    

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
