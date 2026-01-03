class Shirt:
    # Constructor (supports parameterized and parameterless forms)
    def __init__(self, sid=None, sname=None, stype=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.stype = stype     
        self.price = price
        self.size = size       
        print("Shirt object created.")



  # Destructor
    def __del__(self):
        print("Shirt object destroyed.")

    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.stype)
        print("Price:", self.price)
        print("Size:", self.size)