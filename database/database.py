import os
from peewee import SqliteDatabase, PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

#db = SqliteDatabase('usuarios.db')
db = PostgresqlDatabase(os.getenv('DATABASE_URI', ''))