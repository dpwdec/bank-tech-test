class Transaction():
    
    def __init__(self, value, date):
        self.value = value
        self.date = date

    def get_formatted_date(self):
        self.date.strftime("%d/%m/%Y")