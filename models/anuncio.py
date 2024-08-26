from database import connection

def criar_anuncio(usuario_id, titulo, descricao, preco):
    cursor = connection.cursor()
    sql = "INSERT INTO Anuncio (usuario_id, titulo, descricao, preco, dataCriacao) VALUES (%s, %s, %s, %s, NOW())"
    cursor.execute(sql, (usuario_id, titulo, descricao, preco))
    connection.commit()

def obter_anuncios_por_usuario(usuario_id):
    cursor = connection.cursor()
    sql = "SELECT * FROM Anuncio WHERE usuario_id = %s"
    cursor.execute(sql, (usuario_id,))
    return cursor.fetchall()
