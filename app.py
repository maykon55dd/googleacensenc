from flask import Flask, render_template,request,redirect,flash,session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'CRIZINN'


@app.route("/acessoCliente", methods=['POST'])
def acessoCliente():
    email = request.form.get('email')
    senha = request.form.get('text')

    print(f'O Gmail e: {email}')
    print(f'A senha e: {senha}')


