'''
*** Instalações utilizadas ***
- MYSQL Connector/ODBC 8.0 - (mysql-connector-odbc-8.0.26-winx64.msi)
- pip install pyodbc
'''

import pyodbc

conexao = pyodbc.connect(
        "Driver={MySQL ODBC 8.0 ANSI Driver};"
        "Server=localhost;"
        "Database=BANCO_ALIAS;"
        "UID=root;"
        "PWD=SENHA_ROOT;")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM segurados WHERE seguradoid < 51;")
for c in cursor.fetchall():
        print(c)

cursor.close()
conexao.close()

