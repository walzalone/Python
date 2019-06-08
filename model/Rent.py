class Rent:
    def __init__(self,id,renter,book,rentDate,returnDate):
        self.transID = id
        self.renter = renter
        self.book = book
        self.rentDate = rentDate
        self.returnDate = returnDate
    
    def get_book(self):
        return self.book.name
