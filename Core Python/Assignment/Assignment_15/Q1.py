class Book:
    def __init__(self,b_id=101,b_name='Python programming',price=500,author='Guido van Rossum'):

        self.b_id =b_id
        self.b_name=b_name
        self.price=price
        self.author=author
    
    def __del__(self):
        print("DESTRUCTOR CALLED ..........")
    
    def showBook(self):
        
        print("BOOK ID : ",self.b_id)
        print("BOOK NAME : ",self.b_name)
        print("BOOK PRICE : ",self.price)
        print("BOOK AUTHOR : ",self.author)

print(" PARAMETERIZED .....")
b1 = Book(102,'Java Programming',750,'James Gosling')
b1.showBook()

print("parameterless...")
b2 = Book()
b2.showBook()