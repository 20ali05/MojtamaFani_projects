import sqlite3
from datetime import datetime


class customer():
    def __init__(self, name, last_name, phone_number, username , password, wallet):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.wallet = wallet
    @staticmethod    
    def add_customer(customer):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO customer (name , last_name , phone_number, username , password, wallet)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer.name , customer.last_name , customer.phone_number, customer.username , customer.password, customer.wallet)
        )
        conn.commit()
        conn.close()
        wallets_file()
        return f"customer added sucssefuly"
    
    
    @staticmethod
    def check_customer(username, password):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer WHERE username = ? AND password = ?", (username, password))
        cheak = cursor.fetchone()
        conn.close()
        if cheak:
            return True
        else:
            return False
    @staticmethod
    def id_funder(username):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id FROM customer WHERE username = ?', (username,))
        result = cursor.fetchone()
        
        conn.close()
        return result




class items():
    def __init__(self,name, price, description, topic) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.topic = topic
        
    def add_item(item):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO items (name, price, description, topic)
        VALUES (?, ?, ?, ?)
        ''', (item.name, item.price, item.description, item.topic))
        conn.commit()
        conn.close()
        
    def delete_item(id, name):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()

        cursor.execute('''
        DELETE FROM items WHERE id = ? AND name = ?
        ''', (id, name))
        conn.commit()
        conn.close()
        return True
    
    
    
    def update(id , topic, new_data):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        
        query = f"UPDATE items SET {topic} = ? WHERE id = ?"
        cursor.execute(query, (new_data, id))
        if cursor.rowcount == 0:
            print("No item found with the given ID.")
            conn.close()
            return False
        conn.commit()
        conn.close()
        return True
        

    def show_all_items():
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        items = cursor.fetchall()
        conn.close()
        return items


    @staticmethod
    def filter(topic):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM items WHERE topic = ?
        ''', (topic,))
        items = cursor.fetchall()
        conn.close()
        return items




def wallets_file():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT username, wallet FROM customer')
    customers = cursor.fetchall()
    
    conn.close()
    
    with open('wallets.txt', 'w') as file:
        for username, wallet in customers:
            file.write(f"{username}: {wallet}\n")
    
    print("Wallets extracted and saved to wallets.txt")




def check_manager(username, password):
        conn = sqlite3.connect('shop.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM manager WHERE username = ? AND password = ?", (username, password))
        cheak = cursor.fetchone()
        conn.close()
        if cheak:
            return True
        else:
            return False




def create_tables():
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        wallet REAL DEFAULT 0
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS manager (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT NOT NULL,
        topic TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sabad_kharid (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        tedad INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customer(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
        
        
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        tedad INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customer(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
        
      
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        tedad INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customer(id),
        FOREIGN KEY (item_id) REFERENCES items(id)
        
      
    )
    ''')
    conn.commit()
    conn.close()




def add_sabad_kharid(customer_id, item_id, tedad):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    order_date = str(datetime.now())
    status = "not payed yet"
    cursor.execute('''
    INSERT INTO sabad_kharid (customer_id, item_id, tedad, order_date, status)
    VALUES (?, ?, ?, ?, ?)
    ''', (customer_id, item_id, tedad, order_date, status))
    conn.commit()
    conn.close()




def namayessh_daryaft(customer_id, topic):
    list = items.filter(topic)  
    for i in list:
        print(i)
    add_item = input("do you want to add any item into your sabadkharid (y/n): ")
    if add_item.lower() == "y":
        item_id = input("enter the item id: ")
        tedad = input("how many? ")
        add_sabad_kharid(customer_id, item_id, tedad)
    elif add_item.lower() == "n":
        pass




def show_sabad_kharid(customer_id):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM sabad_kharid WHERE customer_id = ? AND status = ?
    ''', (customer_id,"not payed yet"))
    sabad = cursor.fetchall()
    conn.close()
    
    return sabad



  
def hazine_fun(customer_id):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT items.price, sabad_kharid.tedad 
    FROM sabad_kharid
    JOIN items ON sabad_kharid.item_id = items.id
    WHERE sabad_kharid.customer_id = ?
    ''', (customer_id,))
    
    cart_items = cursor.fetchall()
    hazine_kol = 0
    for price, quantity in cart_items:
        hazine_kol += price * quantity
    return hazine_kol




def payment_fun(username, customer_id, hazine):
    with open('wallets.txt', 'r') as file:
            lines = file.readlines()

    updated_lines = []
    user_found = False

    for line in lines:
        parts = line.strip().split(': ')
        if parts[0] == username:
            wallet_now = float(parts[1])
            new_wallet = wallet_now - hazine
            updated_lines.append(f"{username}: {new_wallet}\n")
            user_found = True
        else:
            updated_lines.append(line)

    with open('wallets.txt', 'w') as file:
        file.writelines(updated_lines)
    print(f"Wallet updated for {username}. New balance: {new_wallet}")
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    customer_id = customer.id_funder(username)[0]
    cursor.execute('UPDATE customer SET wallet = ? WHERE username = ?', (new_wallet, username))
    cursor.execute('UPDATE sabad_kharid SET status = ? WHERE customer_id = ?', ("payed", customer_id))

    conn.commit()
    cursor.close()
    return True




def add_orders(customer_id, username):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()


    cursor.execute('''
    SELECT items.name, sabad_kharid.tedad
    FROM sabad_kharid
    JOIN items ON sabad_kharid.item_id = items.id
    WHERE sabad_kharid.customer_id = ?
    ''', (customer_id,))
    
    items = cursor.fetchall()

    with open('orders.txt', 'a') as file:
        file.write(f"Username: {username}\n")
        for item_name, quantity in items:
            file.write(f"{item_name} * {quantity}\n")
        file.write("\n" + "-"*20 + "\n\n")

    conn.close()
    return True




def charge_wallet(customer_id, username, meghdar):
    conn = sqlite3.connect('shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT wallet FROM customer WHERE username = ?', (username,))
    wallet_ghabl = cursor.fetchone()
    wallet_new = wallet_ghabl[0] + meghdar
    
    cursor.execute('UPDATE customer SET wallet = ? WHERE username = ?', (wallet_new, username))
    conn.commit()
    conn.close()
    
    with open('wallets.txt', 'r') as file:
        lines = file.readlines()
    
    updated_lines = []
    user_found = False
    
    for line in lines:
        parts = line.strip().split(': ')
        if parts[0] == username:
            wallet_now = float(parts[1])
            new_wallet = wallet_now + meghdar
            updated_lines.append(f"{username}: {new_wallet}\n")
            user_found = True
        else:
            updated_lines.append(line)
    
    if not user_found:
        updated_lines.append(f"{username}: {meghdar}\n")
    
    with open('wallets.txt', 'w') as file:
        file.writelines(updated_lines)
    
    return True





