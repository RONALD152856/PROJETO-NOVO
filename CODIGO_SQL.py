import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE SITEMA DE RESTAURANTE (nome text,idade integer,email text(")

#cursor.execute("INSERT INTO SISTEMS DE RESTAURANTE VALUES('Maria ,'40, 'maria_123@gmail.com'(")

#banco.commit()
cursor.execute("SELECT * FROM SISTEMA DE RESTAURANTE")
print(cursor.fetchall())