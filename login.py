from flask import Flask, render_template, redirect , request

app = Flask(__name__)

@app.route('/login')
def login():
    nome = request.form.get('username')
    senha = request.form.get('password')

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
