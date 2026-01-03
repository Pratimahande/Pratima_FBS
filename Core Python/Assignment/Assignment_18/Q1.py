class Complex_num:

    def __init__(self,real=0,imag=0):

        self.real=real
        self.imag=imag

    def __add__(self,other):

        real_part= self.real + other.real
        imag_part= self.imag + other.imag 
        return Complex_num(real_part,imag_part)

    def __sub__(self,other):

        real_part= self.real - other.real
        imag_part= self.imag - other.imag 
        return Complex_num(real_part,imag_part)
    
    def show(self):

        print(f"{self.real} + {self.imag}i")

    def __del__(self):

        print("DESTRUCTURE...")

c1 = Complex_num(11,12)
print("complex no : ")
c1.show()
c2 = Complex_num(18,19)
print("complex no : ")
c2.show()

c3 = c1 + c2
print("Addition of complex no. : ")
c3.show()

c4 = c1 - c2 
print("subtraction of complex no. : ")
c4.show()