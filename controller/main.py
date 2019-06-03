from model import Rent
from model import Book as b
import datetime

book1 = b.Book("book1","My First Book")
book2 = b.Book("book2","My Second Book")
book3 = b.Book("book3","My Third Book")

trans1 = Rent(1,"R01",book1,datetime.datetime(2019,6,1),datetime.datetime(2019,6,5))
trans2 = rent(2,"R01",book2,datetime.datetime(2019,6,1),datetime.datetime(2019,6,6))
trans3 = rent(3,"R02",book3,datetime.datetime(2019,6,2),None)

transList = [trans1,trans2,trans3]

def check(renterId,bookId)
    has = hasBook(bookId)
    if has:
        return HasSomeoneRent(renterId,bookId)
    return False


bookList = [book1,book2,book3]

def check(renterId,bookId)
    hasbook = hasBook(bookId)
    if hasBook:
        return hasSomeoneRent(renterId,bookId)
    return False

def hasBook(renterId,bookId)
     for book in bookList:
         if bookId = book.id:
             return True
    return False

def hasSomeoneRent(renterId,bookId)


    for tran in transList:
        if ran.renter == renterId and tran.book == bookId and tran.returnDate < datetime.datetime.now():
            return True
    return False