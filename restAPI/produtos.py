import random
lista_produtos = {
    "Arroz": 5.99,
    "Feijão": 4.50,
    "Macarrão": 3.25,
    "Molho de tomate": 2.00,
    "Azeite de oliva": 10.75,
    "Sal": 1.20,
    "Açúcar": 2.50,
    "Café": 8.99,
    "Leite": 3.75,
    "Queijo": 6.50,
    "Presunto": 7.25,
    "Pão": 2.00,
    "Manteiga": 4.00,
    "Ovos": 5.50,
    "Frango": 9.99,
    "Carne bovina": 12.50,
    "Peixe": 14.75,
    "Batata": 2.25,
    "Cenoura": 1.50,
    "Cebola": 1.00,
    "Alho": 0.75,
    "Tomate": 2.50,
    "Alface": 1.75,
    "Banana": 3.00,
    "Maçã": 2.75,
    "Laranja": 2.50,
    "Morango": 4.50,
    "Abacaxi": 5.00,
    "Limão": 1.25,
    "Melancia": 6.50,
    "Melão": 4.75,
    "Uva": 7.99,
    "Pêssego": 3.50,
    "Mamão": 4.25,
    "Manga": 3.25,
    "Pera": 2.75,
    "Kiwi": 2.99,
    "Abobrinha": 2.00,
    "Berinjela": 1.75,
    "Pepino": 1.25,
    "Brócolis": 2.50,
    "Couve-flor": 3.00,
    "Espinafre": 2.75,
    "Batata-doce": 2.25,
    "Grão-de-bico": 3.75,
    "Lentilha": 3.25,
    "Ervilha": 2.50,
    "Milho enlatado": 1.99,
    "Azeitonas": 4.50,
    "Pipoca": 1.00
}

def produto():
    produto = random.choice(list(lista_produtos.keys()))
    return produto



def preco(produto):
    preco = lista_produtos.get(produto)
    return preco


