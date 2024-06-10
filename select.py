import sqlite3

from main import DB_FILE, TABLE_NAME

# ---------------------------------

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# ---------------------------------
# SELECIONANDO TODOS OS DADOS DA TABELA :
cursor.execute(
    f'SELECT * FROM {TABLE_NAME}' # SELECT = Consulta | * = tudo da Tabela
)

for row in cursor.fetchall(): # row = linha | fetchall = pega TODOS valores.
    _id, name, weight = row
    print(_id, name, weight)


print()

# ---------------------------------
# SELECIONANDO DADOS ESPECIFICOS bDA TABELA :

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"' # DIRECIONO A CONSULTA APENAS PARA O ID 3.
)
row = cursor.fetchone() # fetchone = 1 valor especifico. 
_id, name, weight = row
print(_id, name, weight)

# ---------------------------------

cursor.close()
connection.close()