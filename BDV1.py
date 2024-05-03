import sqlite3

banco = sqlite3.connect('primeiro_banco')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE questões (N°QUESTÃO text, RESPOSTA text)")
#cursor.execute("INSERT INTO questões VALUES('vapoktl','Resposta A')")

#banco.commit()

cursor.execute("SELECT * FROM questões")
print(cursor.fetchall())
