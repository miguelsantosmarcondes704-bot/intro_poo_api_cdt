'''

Criando um banco de dados com PostgreSQL e realizando 
operações básicas utilizando o comando SQL.

1. Criar um banco de dados chamado "exercicio_pratico_BD.db".

2. Criar uma tabela chamada "clientes" com os seguintes campos:

    - id (inteiro, chave primária)
    - nome (texto)
    - email (texto)

    3. Inserir alguns registros na tabela "clientes".

    4. Consultar todos os registros da tabela "clientes"

    5. Atualizar um email de um cliente específico.

    6. Excluir um cliente específico da tabela "clientes".

    7. Consultar novamente todos os registros da tabela "clientes". 
    para verificar as alterações.

    8.Criar uma tabela chamada "pedidos" com os seguintes campos:
    
    - id (inteiro,chave primária)
    - cliente_id (inteiro, chave estrangeira referenciando clientes.id)
    - produto (texto)
    - quantidade (inteiro)

    9. Inserir alguns registros na tabela "pedidos".

    10. Consultar todos os pedidos, incluindo o nome do cliente
    associado a cada pedido.

    11. Atualizar a quantidade de um pedido específico.

    12. Excluir um pedido específico da tabela "pedidos".

    13. Consultar novamente todos os pedidos para verificar as alterações.

    '''

import sqilet3

conn = sqilet3.connect('exercicio_pratico_BD.bd')

cursor = conn.cursor()

cursor.execute(''')
               
               CREATE TABLE OF NOT EXISTS clientes (

               id INTEGER PRIMARY KEY,
               nome TEXT NOT NULL,
               email TEXT NOT NULL

               )

               (''')

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES 
    ('João Silva', 'joao.silva@mail.com'),
    ('Maria Oliveira', 'maria.oliveira@mail.com'),
    ('Carlos Santos', 'carlos.santos@mail.com')
               
               conn.commit()

               cursor.execute('SELECT * FROM clientes )

               clientes = cursor.fetchall()

     print("Clientes:")
     for cliente in clientes:
     print(cliente)
               
               cursor. execute(''')

''')



'''



'''