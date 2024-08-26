import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='usuario_db',
    password='senha_db',
    database='ecommerce',
    cursorclass=pymysql.cursors.DictCursor
)
