import csv

#LEER UN ARCHIVO CSV
"""with open('products.csv',mode='r')as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row) """

#show line by columns
"""with open('products.csv',mode='r')as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(f"Producto:{row['name']}, Precio:{row['price']}, Cantidad:{row['quantity']}") """

#add data
"""new_product={
    'name':'chelaas',
    'price':12,
    'quantity':10,
    'brand':'pilsen',
    'category':'Accesorios',
    'entry_date':'2023-10-01'

}

with open('products.csv',mode='a',newline='')as file:
    file.write("\n")
    csv_writer=csv.DictWriter(file,fieldnames=new_product.keys())
    csv_writer.writerow(new_product)"""


#add new column in the new file

file_path='products.csv'
update_file_path='products_modify.csv'

with open(file_path,mode='r')as file:
    reader=csv.DictReader(file)
    #obtener los nombres de las columnas existentes
    fieldnames=reader.fieldnames+['total_value']
    #crear un nuevo archivo csv con la nueva columna
    with open(update_file_path,mode='w',newline='') as new_file:
        new_file=csv.DictWriter(new_file,fieldnames=fieldnames)
        new_file.writeheader()#escribir la cabecera
        for row in reader:
           row['total_value']=float(row['price'])*float(row['quantity'])
           new_file.writerow(row)