from database import connection

def obter_relatorio_vendas(usuario_id):
    cursor = connection.cursor()
    sql = """
    SELECT a.titulo, COUNT(v.id) AS quantidade_vendida, SUM(v.valor) AS valor_total
    FROM Anuncio a
    JOIN Venda v ON a.id = v.anuncio_id
    WHERE a.usuario_id = %s
    GROUP BY a.id
    """
    cursor.execute(sql, (usuario_id,))
    return cursor.fetchall()
