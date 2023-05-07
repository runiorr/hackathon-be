import sqlite3

# Conectar ao banco de dados 
conn = sqlite3.connect('exemplo.db')

# Criar uma tabela gts
conn.execute('''CREATE TABLE GTS
             (nome TEXT NOT NULL,
              titulo TEXT NOT NULL,
              historia TEXT NOT NULL)''')

nome_usuario ="felipe"
titulo="historia"
texto_mensagem ="emocionante"

#passa para o bando de dados oq foi escrito
conn.execute("INSERT INTO GTS (nome,titulo, historia) VALUES (?, ?, ?)", (nome_usuario,titulo, texto_mensagem))



# Printa tabela
print(conn.execute("""SELECT * FROM GTS""").fetchall())

# Deleta tabela
conn.execute('''DROP TABLE GTS''')

#salva as alterações no banco de dados
conn.commit()

# Fechar a conexão com o banco de dados
conn.close() 
