from fastapi import FastAPI
import psycopg2
app = FastAPI()

conn = psycopg2.connect(dbname = 'mercadinho', user='postgres', password='F4bssguimar@es', host='127.0.0.1')
cursor = conn.cursor()

@app.get('/users/')
def customers():
    cursor.execute('SELECT * FROM Cliente')
    customers = cursor.fetchall()
    return customers

@app.get('/sales/')
def sales():
    cursor.execute('SELECT * FROM Venda')
    sales = cursor.fetchall()
    return sales

@app.get('/sales/{id_venda}')
def get_sale(id_venda: int):
    id_venda -= 1
    cursor.execute('SELECT * FROM Venda')
    sale = cursor.fetchall()
    return sale[id_venda]