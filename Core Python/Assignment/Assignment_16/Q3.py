class Shirt:
    
    sizes={'small': 0 ,'large':20, 'medium': 10}

    def __init__(self,s_id=101,s_name='top',type ='casual',price=900,size='large'):

        self.s_id =s_id
        self.s_name=s_name
        self.type=type
        self.price=price
        self.size=size
        self.price=self.calculate_price()
    
    def __del__(self):

        print("DESTRUCTOR CALLED ..........")
    
    def calculate_price(self):

        f_price=Shirt.sizes.get(self.size,0)
        return self.price + ( self.price * f_price / 100 ) 
        
    
    def showShirt(self):
        
        print("SHIRT ID : ",self.s_id)
        print("SHIRT NAME : ",self.s_name)
        print("SHIRT TYPE : ",self.type)
        print("SHIRT PRICE : ",self.price)
        print("SHIRT SIZE : ",self.size)

print(" PARAMETERIZED .....")
s1 = Shirt(102,'Khurta','traditional',1200,'medium')
s1.showShirt()
print("parameterless...")
s2 = Shirt()
s2.showShirt()