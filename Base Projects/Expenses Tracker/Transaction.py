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


    def __str__(self):
        return f"amount: {'-' * (self.action_type == 'expense') + str(self.amount)}\t\t" \
               f"supplier: {self.supplier}\t\tdescription: {self.description}\t\tdate: {self.date}"


    @classmethod
    def init_from_list(cls, lst: list):
        return Transaction(lst[1], lst[2], lst[3], lst[4], lst[5], uid=lst[0])