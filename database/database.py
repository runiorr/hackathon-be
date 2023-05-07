import sqlite3
from models.gt import GT

def insert_gt(gt: GT):
    
    conn.execute("INSERT INTO GTS (name,title, history) VALUES (?, ?, ?)", (name,title, history))
    #passa para o bando de dados oq foi escrito
    conn.commit()

# Conectar ao banco de dados 
conn = sqlite3.connect('exemplo.db')

try:
    # Criar uma tabela gts
    conn.execute('''CREATE TABLE IF NOT EXISTS GTS
                (name TEXT NOT NULL,
                title TEXT NOT NULL,
                history TEXT NOT NULL)''')

    insert_gts("felipe", "oi","comovai")
    # Printa tabela
    print(conn.execute("""SELECT * FROM GTS""").fetchall())
except Exception as err:
    print(err)
finally:    
    # Deleta tabela
    conn.execute('''DROP TABLE GTS''')

    #salva as alterações no banco de dados
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close() 
