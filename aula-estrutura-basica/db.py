import sqlite3

def conectar():
    conn = sqlite3.connect('escola.db')
    return conn 

def criar_tabela_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS estudantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER
    )
    """
    )
    conn.commit()
    conn.close()
    
def criar_tabela_matricula():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS matricula (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_disciplina TEXT,
        estudante_id INTEGER,
        FOREIGN KEY (estudante_id) REFERENCES estudantes (id)
    )
    """
    )
    conn.commit()
    conn.close()
    
def criar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
    INSERT INTO estudantes (nome, idade) VALUES (?, ?)
    """,
    (nome, idade)
    )
    conn.commit()
    conn.close()
    
def criar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
        INSERT INTO estudantes (nome, idade) VALUES (?, ?)
    """, (nome, idade)
    )
    conn.commit()
    conn.close()
    
def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
    SELECT * FROM estudantes
    """
    )
    estudantes = cursor.fetchall()
    for estudante in estudantes:
        print(estudante)
    conn.commit()
    conn.close() 
    
def criar_matricula(estudante_id, nome_dicisplina):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
    INSERT INTO  matriculas (estudante_id, nome_disciplina) values (?, ?)
    """,(estudante_id, nome_dicisplina)
    )
    conn.commit()
    conn.close()
    
def listar_matricula():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
    """
    SELECT * FROM matriculas JOIN estudantes ON matriculas.estudante_id = estudantes.id
    """
    )
    matriculas = cursor.fetchall()
    for matricula in matriculas:
        print(matricula)
    conn.commit()
    conn.close()