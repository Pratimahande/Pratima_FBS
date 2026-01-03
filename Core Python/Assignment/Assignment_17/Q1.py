class Student:

    def __init__(self,s_id,s_name,age,percentage):

        self.s_id=s_id
        self.s_name=s_name
        self.age=age
        self.percentage=percentage
    
    def accept(self):

        self.s_id=int(input("ENTER THE STUDENT ID : "))
        self.s_name=input("ENTER THE STUDENT NAME : ")
        self.age=input("ENTER THE STUDENT AGE : ")
        self.percentage=float(input("ENTER THE STUDENT PERCENTAGE : "))
    
    def CalculateRank(self):

        if (self.percentage >=85):
            return "Distinction"
        elif(self.percentage >=70):
            return "Frist Class"
        elif(self.percentage >=50):
            return "Second Class"
        elif(self.percentage >=35):
            return "Pass"
        else:
            return "Fail"
    
    def display(self):

        print("STUDENT ID : ",self.s_id)
        print("STUDENT NAME : ",self.s_name)
        print("STUDENT AGE : ",self.age)
        print("STUDENT PERCENTAGE : ",self.percentage)
        print("STUDENT RANK : ",self.CalculateRank())

    def __str__(self):

        print("############################################")
        return(f"STUDENT ID : {self.s_id}\n "
               f"STUDENT NAME : {self.s_name}\n"
               f"STUDENT AGE : {self.age}\n"
               f"STUDENT PERCENTAGE : {self.percentage}\n"
               f"STUDENT RANK : {self.CalculateRank()}\n")  

s1 = Student(101,'Pratima',32,75)
s1.display()

print(s1)       