#from model import Rent, Book as b
import datetime
import importlib.util
rent_spec = importlib.util.spec_from_file_location("Rent", "/home/bank-netforce/test/Python/model/Rent.py")
Rent = importlib.util.module_from_spec(rent_spec)
rent_spec.loader.exec_module(Rent)


book_spec = importlib.util.spec_from_file_location("Book", "/home/bank-netforce/test/Python/model/Book.py")
b = importlib.util.module_from_spec(book_spec)
book_spec.loader.exec_module(b)

def check(renterId,bookId):
    has = hasBook(bookId)
    if has:
        return HasSomeoneRent(renterId,bookId)
    return False

def check(renterId,bookId):
    hasbook = hasBook(bookId)
    if hasBook:
        return hasSomeoneRent(renterId,bookId)
    return False

def hasBook(bookId):
    for book in bookList:
        if bookId == book.id:
            return True
    return False

def hasSomeoneRent(renterId,bookId):
    for tran in transList:
        if tran.renter == renterId and tran.book == bookId and tran.returnDate < datetime.datetime.now():
            return True
    return False

book1 = b.Book("book1","My First Book")
book2 = b.Book("book2","My Second Book")
book3 = b.Book("book3","My Third Book")

trans1 = Rent.Rent(1,"R01",book1,datetime.datetime(2019,6,1),datetime.datetime(2019,6,5))
trans2 = Rent.Rent(2,"R02",book2,datetime.datetime(2019,6,1),datetime.datetime(2019,6,6))
trans3 = Rent.Rent(3,"R03",book3,datetime.datetime(2020,6,2),None)

transList = [trans1,trans2]

bookList = [book1,book2,book3]

check("R01", "book1")


