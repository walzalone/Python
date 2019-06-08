from controller import main
print("===================Start BookRent Program====================")

rentId = input("renter ID :")
#ไส่ process ของผู้เช่า ถ้าจะรับ string ไห้ไส่ 'input' 
bookId = input("book ID :")

canRent = check(renterId,bookId)
#ไส่ process  เช็คว่ายืมได้มั้ย

if(canRent):
    saveTransaction(rentId,bookId)
else:
    print("cannot rent this book")

print("================END==============")
