from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario import criar_usuario, login_usuario, obter_usuario_por_id
from models.anuncio import criar_anuncio, obter_anuncios_por_usuario
from models.relatorio import obter_relatorio_vendas

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if login_usuario(email, senha):
            return redirect(url_for('meu_perfil'))
        else:
            flash('Login inválido.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('index'))

@app.route('/meu_perfil')
@login_required
def meu_perfil():
    usuario = obter_usuario_por_id(session['usuario_id'])
    return render_template('meu_perfil.html', usuario=usuario)

@app.route('/meus_anuncios')
@login_required
def meus_anuncios():
    anuncios = obter_anuncios_por_usuario(session['usuario_id'])
    return render_template('meus_anuncios.html', anuncios=anuncios)

@app.route('/criar_anuncio', methods=['GET', 'POST'])
@login_required
def criar_anuncio():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        preco = request.form['preco']
        criar_anuncio(session['usuario_id'], titulo, descricao, preco)
        return redirect(url_for('meus_anuncios'))
    return render_template('criar_anuncio.html')

@app.route('/relatorio_vendas')
@login_required
def relatorio_vendas():
    relatorio = obter_relatorio_vendas(session['usuario_id'])
    return render_template('relatorio_vendas.html', relatorio=relatorio)

if __name__ == '__main__':
    app.run(debug=True)
