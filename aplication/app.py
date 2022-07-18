import mysql.connector
from decouple import config





conexao = mysql.connector.connect (
    host ='localhost',
    user='Greg',
    password= config('senhasecreta'),
    database='catalogo',

)



cursor = conexao.cursor()


painel = """

Digite a opção

______________________

1 Insir no Banco de Dados
2 Ler Tabela 
3 Alterar Tabela
4 Deletar

______________________
"""

print(painel)

opcao = int(input('Digite uma das seguintes opcoes: '))
    
# Comandos Sql ( CRUD )
# Create
def create():
    nome_produto = input(' Nome do produto para cadastro: ')
    valor = int(input('Valor do produto para cadastro: '))
    comando =f'INSERT INTO vendas(nome_produto,valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)



# Read
def read():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall() # lê o banco de dados
    print ( resultado )



#UpDate
def update():
    nome_produto = input('Qual produto deseja alterar? ')
    valor = int(input('Qual valor do produto? '))
    comando = f'UPDATE vendas SET valor = "{valor}" WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit() # Edita banco de dados



# Delete
def delete():
    idVendas = int(input ('Digite o ID do produto que deseja deletar: '))
    comando = f'DELETE FROM vendas WHERE idVendas = {idVendas}'
    cursor.execute(comando)
    conexao.commit()


if opcao == 1:
    create()
elif opcao == 2:
    read()
elif opcao == 3:
    update()
elif opcao == 4:
    delete()



cursor.close()
conexao.close()