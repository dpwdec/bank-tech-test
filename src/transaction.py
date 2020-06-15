import datetime

class Transaction():
    
    def __init__(self, value, date=datetime.datetime.now()):
        self.value = value
        self.date = date

    def get_formatted_date(self):
        return self.date.strftime("%d/%m/%Y")