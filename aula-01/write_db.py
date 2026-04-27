import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO disciplinas (
        estudante_id, nome
    ) VALUES (?, ?)
    """,
    (1, "Matemática")
)

conn.commit()
conn.close()