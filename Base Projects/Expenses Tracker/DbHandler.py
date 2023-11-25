import sqlite3

from Transaction import Transaction

DB_NAME = "database.db"


def init_db():
    con = sqlite3.connect(DB_NAME)
    con.close()


def get_connection():
    return sqlite3.connect(DB_NAME)


def get_cursor(con: sqlite3.Connection = None):
    if con is None:
        return get_connection().cursor()
    return con.cursor()


def create_table(name, column_names, column_types):
    con = get_connection()

    query = ""
    for i in range(len(column_names)):
        query = query + f"{column_names[i]} {column_types[i]},"

    query = query[:-1]
    query = f'CREATE TABLE {name} ({query})'

    get_cursor(con).execute(query)
    con.commit()
    con.close()


def add_transaction(transaction: Transaction):
    con = get_connection()





