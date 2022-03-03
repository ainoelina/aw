
from re import I
from venv import create
import psycopg2
from config import config

def list_persons(cursor):
	SQL = 'SELECT * FROM person'
	cursor.execute(SQL)
	columns = [desc[0] for desc in cursor.description]
	print()
	print(f"{columns[0]: <5}{columns[1]: <17}{columns[2]: <10}{columns[3]: <10}")
	print()
	content = cursor.fetchall()
	for row in content:
		print(f"{row[0]: <5}{row[1]: <17}{row[2]: <10}{row[3]: <10}")
	print()

def all_person_columns(cursor):
	SQL = 'SELECT * FROM person'
	cursor.execute(SQL)
	columns = [desc[0] for desc in cursor.description]
	for i in columns:
		print(i, end="")
		print(" ", end="")
	print()

def list_certificates(cursor):
	SQL = 'SELECT * FROM certificates'
	cursor.execute(SQL)
	columns = [desc[0] for desc in cursor.description]
	print()
	print(f"{columns[0]: <5}{columns[1]: <17}{columns[2]: <11}")
	print()
	content = cursor.fetchall()
	for row in content:
		print(f"{row[0]: <5}{row[1]: <17}{row[2]: <11}")
	print()

def select_certificate(cursor, certi):
	SQL = f"SELECT person.name, certificates.name FROM certificates INNER JOIN person ON certificates.person_id = person.id WHERE certificates.name = '{certi}'"
	cursor.execute(SQL)
	content = cursor.fetchall()
	for i in content:
		print(f"{i[0]: <10} {i[1]: <5}")

def insert_certificates(con, cursor, cert_name, person_id):
	SQL = f"INSERT INTO certificates (id, name, person_id) VALUES (7, '{cert_name}', {person_id})"
	cursor.execute(SQL)
	con.commit()
	count = cursor.rowcount
	print(f"Added {cert_name} for person_id {person_id}.")

def insert_person(con, cursor, name, age, student):
	SQL = f"INSERT INTO person (name, age, student) VALUES (%s, %s, %s)"
	values = (name, age, student)
	cursor.execute(SQL, values)
	con.commit()

def update_person(con, cursor, name, age, student):
	SQL = "UPDATE person SET age = %s WHERE name = %s"
	values = (age, name)
	cursor.execute(SQL, values)
	con.commit()

def update_certificates(con, cursor, name, person_id):
	SQL = "UPDATE certificates SET name = %s WHERE person_id = %s"
	values = (name, person_id)
	cursor.execute(SQL, values)
	con.commit()
	print(f"")

def delete_person(con, cursor, id):
	SQL = "DELETE FROM person WHERE id = %s"
	cursor.execute(SQL, (id,))
	con.commit()
	print(f"Deleted id: {id} from person database.")

def delete_certificate(con, cursor, id):
	SQL = "DELETE FROM certificates WHERE id = %s"
	cursor.execute(SQL, (id,))
	con.commit()
	print(f"Deleted certificate from id: {id}")

def create_table(con, cursor, table_name):
	SQL = f"CREATE TABLE {table_name} (Id SERIAL PRIMARY KEY,day varchar(255) NOT NULL, temperature int NOT NULL)"
	cursor.execute(SQL)
	con.commit()

def insert_weather(con, cursor, day, temp):
	SQL = "INSERT INTO weather (day, temperature) VALUES (%s, %s)"
	values = (day, temp)
	cursor.execute(SQL, values)
	con.commit()

def list_weather(cursor):
	SQL = 'SELECT * FROM weather'
	cursor.execute(SQL)
	columns = [desc[0] for desc in cursor.description]
	print()
	print(f"{columns[0]: <5}{columns[1]: <12}{columns[2]: <11}")
	print()
	content = cursor.fetchall()
	for row in content:
		print(f"{row[0]: <5}{row[1]: <12}{row[2]: <11}")
	print()

def connect(db_ini, db):
	con = None
	try:
		con = psycopg2.connect(**config(db_ini, db))
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return con

def print_options():
	print("Choose actionn you want to execute:\n")
	print(" Create/insert:\t1 - Create table\t2 - Insert person\t3 - Insert certificate\t\t4 - Insert weather")
	print(" List:\t\t5 - List persons\t6 - List certificates\t7 - List certain certificate\t8 - List weather")
	print(" Update:\t9 - Update person\t10 - Update certificate")
	print(" Delete:\t11 - Delete person\t12 - Delete certificate")
	print(" Quit program:\t-1")
	try:
		action = int(input("Operation: "))
		return action
	except:
		print("\tInvalid operation. Choose valid operation.\n")

def main():
	con = connect('database.ini', 'postgresql')
	cursor = con.cursor()
	while True:
		action = print_options()
		if action == 1:
			create_table(con, cursor, 'weather')
		elif action == 2:
			insert_person(con, cursor, 'kaisa', 60, False)
		elif action == 3:
			insert_certificates(con, cursor, 'AZ-203', 1)
		elif action == 4:
			insert_weather(con, cursor, 'wednesday', 1)
		elif action == 5:
			list_persons(cursor)
		elif action == 6:
			list_certificates(cursor)
		elif action == 7:
			select_certificate(cursor)
		elif action == 8:
			list_weather(cursor)
		elif action == 9:
			update_person(con, cursor, 'aino', 28, None)
		elif action == 10:
			update_certificates(con, cursor, 'AZ-300', 1)
		elif action == 11:
			delete_person(con, cursor, 2)
		elif action == 12:
			delete_certificate(con, cursor, 4)
		elif action == -1:
			break
	cursor.close()
	if con is not None:
		con.close()

main()