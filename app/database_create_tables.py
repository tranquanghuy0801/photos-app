""" Script to create DDL"""
import mysql.connector
from app.config import *

def populate():
	""" create DDL for tables and users """
	print("This script will drop and recreate the photo table.")
	print("")

	drop_table = "DROP TABLE IF EXISTS photo;"
	create_table = """
	create table photo (
	object_key nvarchar(80) not null primary key,
	labels nvarchar(200),
	description nvarchar(200),
	cognito_username nvarchar(150),
	created_datetime DATETIME DEFAULT now()
	);
	"""

	conn = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD,
								   host=DATABASE_HOST,
								   database=DATABASE_DB_NAME)
	cursor = conn.cursor()
	print("Dropping / creating photo table")
	cursor.execute(drop_table)
	conn.commit()
	cursor.execute(create_table)
	conn.commit()

	# conn.close()


populate()
