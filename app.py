from flask import Flask, render_template, redirect, request, flash, session, url_for
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message
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


# Configurações de envio de email com Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tabulendoficial@gmail.com'  # Seu e-mail
app.config['MAIL_PASSWORD'] = 'swnnbmozxervxqcs'  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def enviar_email_para_observadores(observador_email, jogo):
    try:
        msg = Message('Jogo Disponível - TabuLend',
                      sender='tabulendoficial@gmail.com',
                      recipients=[observador_email])
        msg.body = f"O jogo '{jogo.titulo}' está disponível para alugar!"
        mail.send(msg)
        print(f"E-mail enviado para {observador_email}")
    except Exception as e:
        print(f"Falha ao enviar e-mail para {observador_email}. Erro: {e}")



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
    
@app.route('/pesquisarJogos', methods=['GET'])
def pesquisarJogos():
    query = request.args.get('query', '').lower()  # Obtém a consulta da barra de pesquisa

    jogos = JogoDeTabuleiro.catalogoJogos()  # Carrega todos os jogos
    if query:
        # Filtra os jogos cujo título contenha o termo de pesquisa
        jogos_filtrados = [jogo for jogo in jogos if query in jogo.titulo.lower()]
    else:
        jogos_filtrados = jogos  # Se a consulta estiver vazia, exibe todos os jogos

    return render_template('catalogo.html', jogos=jogos_filtrados)

@app.route('/pesquisarJogosAdmin', methods=['GET'])
def pesquisarJogosAdmin():
    query = request.args.get('query', '').lower()  # Obtém a consulta da barra de pesquisa do admin
    jogos = JogoDeTabuleiro.catalogoJogos()  # Carrega todos os jogos

    if query:
        # Filtra os jogos cujo título contenha o termo de pesquisa
        jogos_filtrados = [jogo for jogo in jogos if query in jogo.titulo.lower()]
    else:
        jogos_filtrados = jogos  # Se a consulta estiver vazia, exibe todos os jogos

    return render_template('catalogoadmin.html', jogos=jogos_filtrados)

@app.route('/adicionarJogo')
def adicionarjogo():
    return render_template('telaCadastrarJogo.html')

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')

@app.route('/voltaradmin')
def voltaradmin():
    return render_template('telaadmin.html')

@app.route('/catalogoadmin')
def catalogoadmin():
    jogos = JogoDeTabuleiro.catalogoJogos()
    return render_template('catalogoadmin.html',jogos=jogos)

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
        novoJogo.salvarJogoNovo()

        return redirect('/Adminlogado')

    flash('Tipo de arquivo de imagem não permitido.')
    return redirect(request.url)


@app.route('/editarJogo/<titulo>', methods=['GET', 'POST'])
def editarJogo(titulo):
    if request.method == 'GET':
        jogos = JogoDeTabuleiro.catalogoJogos()
        jogo = next((j for j in jogos if j.titulo == titulo), None)
        if jogo:
            return render_template('editarjogo.html', jogo=jogo)
        else:
            flash('Jogo não encontrado.')
            return redirect('/Adminlogado')
    
    if request.method == 'POST':
        titulo_novo = request.form.get('titulo')
        editora = request.form.get('editora')
        preco = request.form.get('valor')
        status = request.form.get('status')
        imagem = request.files.get('imagem')

        if imagem and extensaovalida(imagem.filename):
            filename = secure_filename(imagem.filename)
            imagem.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            caminho_imagem = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        else:
            caminho_imagem = request.form.get('imagem_atual')

        # Atualiza os dados do jogo
        jogos = JogoDeTabuleiro.catalogoJogos()
        jogo = next((j for j in jogos if j.titulo == titulo), None)
        if jogo:
            jogo.titulo = titulo_novo
            jogo.editora = editora
            jogo.preco = preco
            jogo.status = status
            jogo.imagem = caminho_imagem
            salvar_jogo(jogos)
            jogo.alterarDisponibilidade(status)

            return render_template('telaadmin.html', jogos=jogos)
        else:
            flash('Jogo não encontrado.')
            return redirect('/Adminlogado')
        
        
@app.route('/excluir_jogo/<titulo>', methods=['POST'])        
def excluir_jogo(titulo):
    jogos = JogoDeTabuleiro.catalogoJogos()
    jogo_a_excluir = next((jogo for jogo in jogos if jogo.titulo == titulo), None)

    if jogo_a_excluir:
        # Remover o jogo da lista
        jogos.remove(jogo_a_excluir)
        # Salvar a lista de jogos atualizada
        salvar_jogo(jogos)

        flash(f'O jogo "{titulo}" foi excluído com sucesso.')
        return redirect('/Adminlogado')
    else:
        flash(f'O jogo "{titulo}" não foi encontrado.')
        return redirect('/Adminlogado')
    
@app.route('/notificar/<titulo>', methods=['POST'])
def notificar(titulo):
    username = session.get('username')
    if not username:
        flash("Você precisa estar logado para ser notificado.")
        return redirect('/')

    email_do_usuario = buscar_email_do_usuario(username)
    if not email_do_usuario:
        flash('email do usuario nao encotrado')
        return redirect('/usuariologado')


    jogos = JogoDeTabuleiro.catalogoJogos()  # Supondo que você tenha um catálogo de jogos
    jogo = next((j for j in jogos if j.titulo == titulo), None)

    if jogo:
        jogo.AddObsrvadores(email_do_usuario)  # Adiciona o e-mail à lista de observadores
        flash(f"Você será notificado quando o jogo {titulo} estiver disponível.")
    else:
        flash("Jogo não encontrado.")

    return redirect('/usuariologado')


@app.route('/alterar_status/<titulo>', methods=['POST'])
def alterar_status(titulo):
    jogos = JogoDeTabuleiro.catalogoJogos()
    jogo = next((j for j in jogos if j.titulo == titulo), None)

    if jogo:
        jogo.alterarDisponibilidade(alugado=False)  # Torna o jogo disponível
        flash(f"O jogo {titulo} está agora disponível.")
        salvar_jogo(jogos)
    else:
        flash("Jogo não encontrado.")
    
    return redirect('/Adminlogado')

def salvar_jogo(jogos):
    with open(jogos_path, 'w') as file:
        for jogo in jogos:
            observadores_str = ','.join(jogo.observadores)
            file.write(f"titulo: {jogo.titulo}, editora: {jogo.editora}, preco: {jogo.preco}, status: {jogo.status}, imagem: {jogo.imagem}, observadores: {observadores_str}\n")
    

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
