'''
*** Instalações utilizadas ***
- SQL Server Management Studio (SSMS) - (SSMS-Setup-PTB.exe)
- pip install pyodbc
'''

import pyodbc

conexao = pyodbc.connect("Driver={SQL Server};"
        "Server=NOTE-FLAVIO\MSSQLSERVER2;"
        "Database=BANCO_NOME;")

# *** caso precisasse de login e senha ***
# conexao = pyodbc.connect("Driver={SQL Server};"
#            "Server=NOTE-FLAVIO\MSSQLSERVER2;"
#            "Database=BANCO_ALIAS;"
#            "UID=LOGIN;"
#            "PWD=SENHA;")

cursor = conexao.cursor()

cursor.execute('SELECT * FROM dbo.clientes WHERE codcli < 51')
for c in cursor.fetchall():
        print(c)

cursor.close()
conexao.close()