import json

#leer json
"""with open('products.json','r') as file:
    produscts=json.load(file)
    #mostrar el contenido
    for product in produscts:
        print(f"Producto:{product['name']}, Precio:{product['price']}, Cantidad:{product['quantity']}")"""

#add data json

new_product={
        "name": "HELLO WORLD",
        "price": 150,
        "quantity": 25,
        "brand": "SoundMax",
        "category": "Audio",
        "entry_date": "2024-03-15"
    }
products=[]
with open('products.json','r') as file:
    products=json.load(file)
    products.append(new_product)
with open('products-update.json','w') as newfile:
    json.dump(products,newfile,indent=2)
