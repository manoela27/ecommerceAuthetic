from werkzeug.security import generate_password_hash, check_password_hash
from database import connection

def criar_usuario(nome, email, senha):
    senha_hash = generate_password_hash(senha)
    cursor = connection.cursor()
    sql = "INSERT INTO Usuario (nome, email, senha, dataCadastro) VALUES (%s, %s, %s, NOW())"
    cursor.execute(sql, (nome, email, senha_hash))
    connection.commit()

def login_usuario(email, senha):
    cursor = connection.cursor()
    sql = "SELECT * FROM Usuario WHERE email = %s"
    cursor.execute(sql, (email,))
    usuario = cursor.fetchone()
    
    if usuario and check_password_hash(usuario['senha'], senha):
        session['usuario_id'] = usuario['id']
        session['nome'] = usuario['nome']
        return True
    return False

def obter_usuario_por_id(usuario_id):
    cursor = connection.cursor()
    sql = "SELECT * FROM Usuario WHERE id = %s"
    cursor.execute(sql, (usuario_id,))
    return cursor.fetchone()
