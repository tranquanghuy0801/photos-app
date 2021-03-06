"Database layer"
import mysql.connector
from app.config import *

def list_photos(cognito_username):
    "Select all the photos from the database"
    conn = get_database_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""SELECT object_key, description, labels, created_datetime
        FROM photo WHERE cognito_username = %s
        ORDER BY created_datetime desc""", (cognito_username,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def add_photo(object_key, labels, description, cognito_username):
    "Add a photo to the database"
    conn = get_database_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""INSERT INTO photo (object_key, labels, description, cognito_username) VALUES
    (%s, %s, %s, %s);""", (object_key, labels, description, cognito_username))
    conn.commit()
    cursor.close()
    conn.close()

def delete_photo(object_key, cognito_username):
    "Delete a photo.  Users can only delete their photos!"
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM photo WHERE object_key = %s AND cognito_username = %s;""",
                   (object_key, cognito_username))
    conn.commit()
    cursor.close()
    conn.close()

def get_database_connection():
    "Build a database connection"
    conn = mysql.connector.connect(user=DATABASE_USER, password=DATABASE_PASSWORD,
                                   host=DATABASE_HOST,
                                   database=DATABASE_DB_NAME,
                                   use_pure=True) # see https://bugs.mysql.com/90585
    return conn
