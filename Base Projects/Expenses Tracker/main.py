import datetime
import sys

from Transaction import Transaction
import DbHandler


def create_transaction():
    choice = int(input("Enter 1 for income or 2 for expense: "))
    action_type = "income" if choice == 1 else "expense"
    supplier = input("Enter the supplier of the transaction: ")
    amount = float(input("Enter amount (positive value): "))
    date = input("Enter Transaction date(dd-mm-yyyy): ")
    description = input("Enter short description: ")
    transaction = Transaction(action_type, supplier, amount, date, description)
    DbHandler.add_transaction(transaction, override=True)


def main_app():
    action = int(input("Enter which operation to do: "))  # TODO: add options
    while action != -1:
        if action == 1:
            create_transaction()
        action = int(input("Enter which operation to do: "))


def init_app():
    DbHandler.init_db()
    DbHandler.create_table("Transactions",
                           ["Uid", "type", "supplier", "amount", "date", "description"],
                           ["text NOT NULL PRIMARY KEY", "text", "text", "real", "date", "text"])
    print("Initialization completed!")



def main():
    argv = sys.argv
    if len(argv) > 1:
        if argv[1] == "init":
            init_app()
    else:
        main_app()



if __name__ == '__main__':
    main()
