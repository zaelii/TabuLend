from flask import Flask, render_template,redirect , request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NLETESTE'

DadosLogin = 'DadosLogin.txt'

@app.route('/')
def home():
    return render_template('telalogin.html')

@app.route('/login', methods=['POST'])
def login():
    nome = request.form.get('username')
    senha = request.form.get('password')
    print(nome)
    print(senha)
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    nome = request.form.get('name')
    email = request.form.get('email')
    usuario = request.form.get('username')
    senha = request.form.get('password')

    with open(DadosLogin, 'a') as f:
        f.write(f'Nome: {nome}, Email: {email}, Usuario: {usuario} Senha: {senha}\n')

    return render_template('catalogo.html')

if __name__ == '__main__':
    if not os.path.exists(DadosLogin):
        with open(DadosLogin, 'w') as f:
            f.write("Cadastro de Usuários:\n")
    app.run(debug=True)


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
    app.run(debug=True)
