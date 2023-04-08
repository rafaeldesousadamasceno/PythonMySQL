import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("SHOW TABLES")
"""
for x in mycursor:
  print(x)
"""

"""
========================= INSERINDO 01 REGISTRO ========================
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Rafael", "Rua Antonia Botelho")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Registro Inserido!")
"""

"""
========================= INSERINDO VÁRIOS REGISTROS ========================
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
"""

"""
======================== MOSTRANDO O ID DO ÚLTIMO REGISTRO INSERIDO =======
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)
"""
"""
==============================SELECIONANDO MUITOS E APENAS UM REGISTRO ======
# mycursor.execute("SELECT * FROM customers")
mycursor.execute("SELECT name, address FROM customers")

#myresult = mycursor.fetchall()
myresult = mycursor.fetchone()


for linha in myresult:
    print(linha)

print(myresult)
"""

"""
======================= EXCLUINDO REGISTRO COM CONDICIONAL =============
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

======================= EXCLUINDO REGISTRO COM CONDICIONAL E SQL INJECTION =============
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
"""

"""
==================== EXCLUINDO TABELA =======================
sql = "DROP TABLE customers"

mycursor.execute(sql)
"""

"""
==================== EXCLUINDO TABELA SOMENTE SE EXISTIR ==============
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
"""

"""
=================== ATUALIZANDO TABELA COM PREVENÇÃO DE SQL INJECTION ===
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
"""
