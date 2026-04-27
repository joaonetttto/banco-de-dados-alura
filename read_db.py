import sqlite3
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM disciplinas")
conn.commit()
disciplinas = cursor.fetchall()
print(disciplinas)

    
conn.close()