'''
*** Instalações utilizadas ***
- pip install firebirdsql
- firebird_v2.5 (Firebird-2.5.exe)
'''

import firebirdsql

conexao = firebirdsql.connect(
        host='127.0.0.1',
        database=r'C:\SISTEMA\BD\dados.fdb',
        port=3051,
        user='USUARIO_BD',
        password='SENHA_BD',
        charset="ISO8859_1")

cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes WHERE codigo < 51")
for c in cursor.fetchall():
        print(c)

cursor.close()
conexao.close()