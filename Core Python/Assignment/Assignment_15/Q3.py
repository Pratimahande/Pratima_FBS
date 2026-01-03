class Shirt:
    def __init__(self,s_id=101,s_name='Khurta',type ='Traditional',price=1000,size='large'):

        self.s_id =s_id
        self.s_name=s_name
        self.type=type
        self.price=price
        self.size=size
    
    def __del__(self):
        print("DESTRUCTOR CALLED ..........")
    
    def showShirt(self):
        
        print("SHIRT ID : ",self.s_id)
        print("SHIRT NAME : ",self.s_name)
        print("SHIRT TYPE : ",self.type)
        print("SHIRT PRICE : ",self.price)
        print("SHIRT SIZE : ",self.size)

print(" PARAMETERIZED .....")
s1 = Shirt(102,'suit','formal',3000,'Small')
s1.showShirt()

print("parameterless...")
s2 = Shirt()
s2.showShirt()