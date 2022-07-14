import mysql.connector
from CRUD.validate import func

# Criando a conexão entre o BD e o PY
class connect:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='crud'
        )
        self.cursor = self.conn.cursor()


# CRUD
# CREATE
def insert(name_product, price):
    conn = connect()
    command = f' INSERT INTO sales (name_product, price) VALUES ("{name_product}", {price})'
    conn.cursor.execute(command)
    # Edita o banco de dados
    conn.conn.commit()


# READ
def read(table):
    conn = connect()
    command = f' select * from {table} order by id_product;'
    conn.cursor.execute(command)
    # Lê o banco de dados
    result = conn.cursor.fetchall()
    return result


# UPDATE
def update(att, id_product):
    conn = connect()
    if func.checknumeric(func.convert(att)):
        opt = 'price'
    else:
        opt = 'name_product'
    command = f' UPDATE sales SET {opt} = "{att}" WHERE id_product = {id_product}'
    conn.cursor.execute(command)
    conn.conn.commit()


# DELETE
def delete(id_product):
    conn = connect()
    command = f' DELETE FROM sales WHERE id_product = {id_product}'
    conn.cursor.execute(command)
    conn.conn.commit()


# 'Fechando' o banco de dados
def close():
    conn = connect()
    conn.conn.close()
    conn.cursor.close()


