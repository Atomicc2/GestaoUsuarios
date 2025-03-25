from peewee import Model, CharField, DateTimeField
from database.database import db
from datetime import datetime


class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_registro = DateTimeField(default=datetime.now)

    class Meta:
        database = db