# Clearing the screen
import os
os.system('clear')


# Importing sqlite3 module
import sqlite3


def add_one(first_name,last_name,email):
	# Establishing a connection and create DB
	conn = sqlite3.connect('customer.db')

	# Creating a cursor
	c = conn.cursor()

	c.execute("INSERT INTO customers VALUES (?,?,?)", (first_name,last_name,email) )

	# Commiting changes made
	conn.commit()

	# Closing our connection
	conn.close() 


def create_table():
	# Establishing a connection and create DB
	conn = sqlite3.connect('customer.db')

	# Creating a cursor
	c = conn.cursor()

	# Create a table
	c.execute(""" CREATE TABLE customers (
			first_name text,
			last_name text,
			email text
		)""")

	# Commiting changes made
	conn.commit()

	# Closing our connection
	conn.close()



def insert_records():
	# Establishing a connection and create DB
	conn = sqlite3.connect('customer.db')

	# Creating a cursor
	c = conn.cursor()

	# Inserting multiple rows
	customers = [
				('Jason', 'Bourne', 'jason@email.com'), 
				('James', 'Bond', 'james@email'), 
				('Red', 'Sparrow', 'red@email'), 
				('Nathan', 'Muir', 'nathan@email.com')
			]

	c.executemany("INSERT INTO customers VALUES (?,?,?)", customers)

	# Commiting changes made
	conn.commit()

	# Closing our connection
	conn.close()




# This functin will query the database and return all records
def show_records():
	# Establishing a connection and create DB
	conn = sqlite3.connect('customer.db')

	# Creating a cursor
	c = conn.cursor()

	# Querying
	c.execute("SELECT rowid, * FROM customers")

	items = c.fetchall()

	for item in items:
		print(item)

	# Commiting changes made
	conn.commit()

	# Closing our connection
	conn.close()



def del_record():



