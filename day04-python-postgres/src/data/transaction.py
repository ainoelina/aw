import psycopg2
from config import config


def connect(db_ini, db):
	con = None
	try:
		con = psycopg2.connect(**config(db_ini, db))
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return con

def transaktio(con, cursor, src, dest, amount):
	SQL = "SELECT saldo FROM bank WHERE name = %s"
	values = (src,)
	cursor.execute(SQL, values)
	record = int(cursor.fetchone()[0])
	record = record - amount
	SQL_withdraw = "UPDATE bank SET saldo = %s WHERE name = %s"
	values = (record, src)
	cursor.execute(SQL_withdraw, values)

	SQL = "SELECT saldo FROM bank WHERE name = %s"
	values = (dest,)
	cursor.execute(SQL, values)
	record = int(cursor.fetchone()[0])
	record = record + amount
	SQL_credit = "UPDATE bank SET saldo = %s WHERE name = %s"
	values = (record, dest)
	cursor.execute(SQL_credit, values)
	con.commit()

def list_accounts(cursor):
	SQL = 'SELECT * FROM bank'
	cursor.execute(SQL)
	columns = [desc[0] for desc in cursor.description]
	print()
	print(f"{columns[0]: <5}{columns[1]: <17}{columns[2]: <11}")
	print()
	content = cursor.fetchall()
	for row in content:
		print(f"{row[0]: <5}{row[1]: <17}{row[2]: <11}")
	print()

def main():
	con = connect('database.ini', 'postgresql')
	cursor = con.cursor()
	list_accounts(cursor)
	transaktio(con, cursor, 'sara', 'aino', 600)
	list_accounts(cursor)
	cursor.close()
	if con is not None:
		con.close()

main()