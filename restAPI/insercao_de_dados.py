import psycopg2
from faker import Faker
import random
import produtos as pd

fake = Faker()
conn = psycopg2.connect(dbname = 'mercadinho', user='postgres', password='F4bssguimar@es', host='127.0.0.1')

cursor = conn.cursor()

for _ in range(20):
    nome = fake.name()
    cpf = fake.numerify(text='###.###.###-##')
    cursor.execute("INSERT INTO Cliente (nome, cpf)VALUES (%s, %s)",
         (nome, cpf))


conn.commit()
       

    
cursor.execute("SELECT id FROM Cliente")
ids_clientes = [row[0] for row in cursor.fetchall()]


for _ in range(20):
    produto = pd.produto()
    preco_unitario = pd.preco(produto)
    quantidade = random.randint(1,10)
    cliente_id = random.choice(ids_clientes)
    valor_total = preco_unitario * quantidade
    cursor.execute("INSERT INTO Venda (produto, preco_unitario, quantidade,cliente_id,valor_total) VALUES (%s, %s, %s, %s, %s)",
         (produto, preco_unitario, quantidade,cliente_id,valor_total))

conn.commit()