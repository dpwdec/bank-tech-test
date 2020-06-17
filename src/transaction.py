import datetime

class Transaction():
    
    def __init__(self, value, date=datetime.datetime.now()):
        self.value = value
        self.date = date
    
    def is_debit(self):
        if self.value < 0: return False
        return True
