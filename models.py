from peewee import *

# database connection
db = SqliteDatabase("zomato.db")


class User(Model):
    user_name = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


# def create_tables():
#     # create tables in sqlite db
#     with db:
#         db.create_tables([User])

db.create_tables([User])