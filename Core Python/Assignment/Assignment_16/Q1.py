class Book:
    count = 0
    def __init__(self,b_id=101,b_name='C Programming',author='Dennis Ritchie',price=700):

        self.b_id =b_id
        self.b_name=b_name
        self.price=price
        self.author=author
        Book.count +=1
    
    def __del__(self):
        print("DESTRUCTOR CALLED ..........")
    
    def showBook(self):
        
        print("BOOK ID : ",self.b_id)
        print("BOOK NAME : ",self.b_name)
        print("BOOK PRICE : ",self.price)
        print("BOOK AUTHOR : ",self.author)

print(" PARAMETERIZED .....")
b1 = Book(102,'PHP Programming','Rasmus lerdorf',500)
b1.showBook()

print("parameterless...")
b2 = Book()
b2.showBook()

print("total of books object created :",Book.count)