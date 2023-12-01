import datetime
import sys

from Transaction import Transaction
import DbHandler
import Utilities


def enter_transaction():
    choice = int(input("Enter 1 for income or 2 for expense: "))
    action_type = "income" if choice == 1 else "expense"
    supplier = input("Enter the supplier of the transaction: ")
    amount = float(input("Enter amount (positive value): "))
    date = input("Enter Transaction date(dd-mm-yyyy): ")
    description = input("Enter short description: ")
    transaction = Transaction(action_type, supplier, amount, date, description)
    result, response = DbHandler.add_transaction(transaction, override=True)
    if not result:
        choice = int(input(response + "\nenter 1 to try again or 0 to go back to main menu: "))
    else:
        choice = int(input(response + "\nenter 1 to add another transaction or 0 to go back to main menu: "))
    if choice == 1:
        enter_transaction()
    else:
        return


def show_all_transactions():
    result, lst = DbHandler.get_all_transactions()
    if result:
        print("all listed transaction:")
        for index, transaction in enumerate(lst):
            print(f"{index+1}) {transaction}")
    else:
        print("An error occurred, pls try again")
    return




def main_app():
    action = int(input(Utilities.MENU_UI_TEXT))  # TODO: add options
    while action != -1:
        print()
        if action == 1:
            enter_transaction()
        if action == 2:
            show_all_transactions()
        print()
        action = int(input(Utilities.MENU_UI_TEXT))


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
