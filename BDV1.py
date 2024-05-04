import sqlite3


conn = sqlite3.connect('questionario.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Perguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT,
    opcao_a TEXT,
    opcao_b TEXT,
    opcao_c TEXT,
    opcao_d TEXT,
    resposta_correta TEXT
)
''')
perguntas = [
    ("A atual legislação de trânsito intitula-se:", "A) Código Nacional de Trânsito", "B) Código de Trânsito", "C) Código de Trânsito Brasileiro", "D) Código Brasileiro de Trânsito", "C"),
("A atual legislação de trânsito intitula-se:", "A) Código Nacional de Trânsito", "B) Código de Trânsito", "C) Código de Trânsito Brasileiro", "D) Código Brasileiro de Trânsito", "C")
("A atual legislação de trânsito intitula-se:", "A) Código Nacional de Trânsito", "B) Código de Trânsito", "C) Código de Trânsito Brasileiro", "D) Código Brasileiro de Trânsito", "C")





]

for pergunta in perguntas:
    cursor.execute(
        'INSERT INTO Perguntas (pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta) VALUES (?, ?, ?, ?, ?, ?)',
        pergunta)
conn.commit()

print("Banco de dados criado e perguntas inseridas com sucesso!")

cursor.execute("SELECT * FROM Perguntas")
print(cursor.fetchall())

import sqlite3

conn = sqlite3.connect('questionario.db')
cursor = conn.cursor()




id_pergunta = 1


cursor.execute("SELECT * FROM Perguntas WHERE id=?", (id_pergunta,))


pergunta = cursor.fetchone()


if pergunta:
    print("Pergunta encontrada:", pergunta)
else:
    print("Pergunta não encontrada.")


conn.close()
