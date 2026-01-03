class Product:

    discount = 10

    def __init__(self,p_id=1,p_name='fan',price=50000,quntity=2):

        self.p_id=p_id
        self.p_name=p_name
        self.price=price
        self.quntity=quntity
    
    def __del__(self):
        
        print("DISTRUCTOR CALLED......")
    
    def showProduct(self):

        print("PRODUCT ID : ",self.p_id)
        print("PRODUCT NAME : ",self.p_name)
        print("PRODUCT PRICE : ",self.price)
        print("PRODUCT QUNTITY: ",self.quntity)
    
    def applay_discount(self):

        discount_amt=(self.price * Product.discount) / 100
        self.price = self.price - discount_amt
        return discount_amt

print("Parameterized....")
p1 = Product(102,'Cooler',50000,3)

print("befored discount..")
p1.showProduct()
print("##################################")
print("after discount")
p1.applay_discount()
p1.showProduct()

print("##################################")
print("parameterless.....")

p2 = Product()
print("befored discount..")
p2.showProduct()
print("##################################")
print("after discount")
p2.applay_discount()
p2.showProduct()
    