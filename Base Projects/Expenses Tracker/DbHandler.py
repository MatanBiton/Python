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


# TODO: check for multiple entries
def add_transaction(transaction: Transaction, override=False):
    con = get_connection()
    if override:
        query = f"INSERT INTO Transactions VALUES ('{transaction.uid}', '{transaction.action_type}'," \
                f" '{transaction.supplier}', '{transaction.amount}', '{transaction.date}', '{transaction.description}')"
        try:
            con.cursor().execute(query)
            con.commit()
        except sqlite3.Error:
            con.close()
            return False, "Operation failed!"
        con.close()
        return True, "transaction added successfully!"
    else:
        con.close()
        pass


def get_all_transactions():
    query = "SELECT * FROM Transactions"
    con = get_connection()
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    result = cur.fetchall()
    cur.close()
    con.close()
    if result is None:
        return False, "error"
    else:
        return True, [Transaction.init_from_list(lst) for lst in result]





