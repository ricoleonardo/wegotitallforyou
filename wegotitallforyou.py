import sqlite3

conn =sqlite3.connect('wegotitallforyou.db')
cursor = conn.cursor()

#print('Open databse successfully')

#create_table_query = "CREATE TABLE EMPLOYEES"

# Create Tables
cursor.execute(''' CREATE TABLE IF NOT EXISTS vendors (id INTEGER PRIMARY KEY, name varchar)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name varchar, vendors_id INTEGER, description text)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS invoices (id INTEGER PRIMARY KEY, sales_reps_id INTEGER, customers_id INTEGER, products_id INTEGER)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS sales_reps (id INTEGER PRIMARY KEY, name varchar)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name varchar)''')

quit = False

while not quit :
    print ("We Got It All For You")
    while True:
        choosetable = input('Please choose a table to add entry: Type (v) for Vendors, (p) for products, (ve) to view entry and (q) to exit: ')
        if choosetable.lower() == "v":
            name = input("Vendors Name: ")
            cursor.execute('INSERT INTO vendors (name) VALUES (?)', [name])
            conn.commit()
            continue
        elif choosetable.lower() == "p":
            name = input("Product name: ")
            vendors_id = input("Vendor ID: ")
            description = input("Description: ")
            cursor.execute('INSERT INTO products (name, vendors_id, description) VALUES (?, ?, ?)', (name, vendors_id, description))
            conn.commit()
            continue

        elif choosetable.lower() == "ve":
            whattoview = int(input("Choose (1) for Vendors List or (2) for Products: "))
            if whattoview == 1:
                cursor.execute('SELECT * FROM vendors')
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            elif whattoview == 2:
                cursor.execute('SELECT * FROM products')
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        
        elif choosetable.lower() == "q":
            quit = True
            break


        else:
            print("Invalid Input")
            continue
            




