# SERVIDOR : SQLite
# BASE DE DADOS : ARQUIVOS
# TABELA : COLUNAS


import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3' # NOME DA BASE DE DADOS. 
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers' # NOME DA TABELA

connection = sqlite3.connect(DB_FILE) # CRIA UMA CONEXAO. 
cursor = connection.cursor() 
# CURSOR : INTERAGIR COM A BD.
# Executar comandos, obter resultados, inserir, atualizar, deletar dados ...

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# ---------------------------------

# CUIDADO: FAZENDO DELETE SEM WHERE | PERIGOSO. 
cursor.execute( # EXECUTE = Executar comandos na TABELA. 
    f'DELETE FROM {TABLE_NAME}' # Comando para Deletar TODOS os DADOS.
)

# DELETE MAIS CUIDADOSO | MAIS SEGURO
cursor.execute( # Comando para RESETAR o AUTO-INCREMENTO.
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# ---------------------------------
# Cria a tabela
# SQL

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,' # COLUNA 1
    'name TEXT,'  # COLUNA 2
    'weight REAL' # COLUNA 3
    ')'
)
connection.commit()

# ---------------------------------
# Registrar valores nas colunas da tabela
# CUIDADO: sql injection (SIMPLIFICANDO : Quando o usuario injeta o dado)

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)' # bindings ou placeholders, etc ...
)


# cursor.execute(sql, ['Joana', 4]) # execute realiza 1 comando.
# cursor.executemany( # executemany = realiza +1 comando.
#     sql,
#     (
#         ('Joana', 4), ('Luiz', 5)
#     )
# )
cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
cursor.executemany(sql, (
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
))

# cursor.execute ou cursor.executemany
# Chama a variavel "sql", passando : name + weight.
# estrutura com mais seguranca aos dados.

connection.commit()

# ---------------------------------


if __name__ == '__main__':
    print(sql)


    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 1'
    )

    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} ' # EDITA A TABELA
        'SET name="QUALQUER", weight=67.89 ' # NOS CAMPOS : NAME | WEIGTH
        'WHERE id = 2' # NA LINHA 2 | NO ID 2
    )

    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()