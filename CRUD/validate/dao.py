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
    name = f'select name_product from sales where name_product = "{name_product}";'
    conn.cursor.execute(name)
    nameexist = conn.cursor.fetchall()
    if nameexist:
        return True
    else:
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
    # VALIDANDO NOME DO PRODUTO
    if opt == 'name_product':
        name(att)
        if name(att):
            pass
        else:
            command = f' UPDATE sales SET {opt} = "{att}" WHERE id_product = {id_product}'
            conn.cursor.execute(command)
            conn.cursor.fetchall()
    # SE FOR PREÇO EXECUTA
    if opt == 'price':
        command = f' UPDATE sales SET {opt} = "{att}" WHERE id_product = {id_product}'
        conn.cursor.execute(command)
        conn.cursor.fetchall()


# DELETE
def delete(id_product):
    conn = connect()
    id = f'select id_product from sales where id_product = "{id_product}";'
    conn.cursor.execute(id)
    idexist = conn.cursor.fetchall()
    if idexist:
        command = f' DELETE FROM sales WHERE id_product = "{id_product}"'
        conn.cursor.execute(command)
        conn.conn.commit()


# VALIDANDO ID
def id(id_product):
    conn = connect()
    id = f'select id_product from sales where id_product = "{id_product}";'
    conn.cursor.execute(id)
    idexist = conn.cursor.fetchall()
    if not idexist:
        return True
    else:
        return False


# VALIDANDO NOME
def name(name_product):
    conn = connect()
    name = f'select name_product from sales where name_product = "{name_product}";'
    conn.cursor.execute(name)
    nameexist = conn.cursor.fetchall()
    if nameexist:
        return True
    else:
        return False


# 'Fechando' o banco de dados
def close():
    conn = connect()
    conn.conn.close()
    conn.cursor.close()
