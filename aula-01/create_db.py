import sqlite3

conn = sqlite3.connect('escola.db') #cria e depois conceta com o banco de dados

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS estudantes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
    """)

cursor.execute(
    
    """
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        estudante_id INTEGER,
        FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
    )
    """
)

conn.commit() #salva as alterações no banco de dados
conn.close() #fecha a conexão com o banco de dados