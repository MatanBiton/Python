from hashlib import sha256


class Transaction:

    def __init__(self, action_type: str, supplier: str, amount: float, date: str, description: str,
                 uid: str = ""):
        self.action_type = action_type
        self.supplier = supplier
        self.amount = amount
        self.date = date
        self.description = description
        self.uid = self.__generate_uid() if uid == "" else uid



    def __generate_uid(self):
        data: str = self.action_type + self.supplier + str(self.amount) + self.description
        return sha256(data.encode('utf-8')).hexdigest()
