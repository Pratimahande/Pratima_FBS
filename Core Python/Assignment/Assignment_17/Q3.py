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

        return(f"STUDENT ID : {self.s_id}\n "
               f"STUDENT NAME : {self.s_name}\n"
               f"STUDENT AGE : {self.age}\n"
               f"STUDENT PERCENTAGE : {self.percentage}\n"
               f"STUDENT RANK : {self.CalculateRank()}")  

class Medical(Student):

    def __init__(self, stu_id, stu_name, stu_age, stu_percentage, sepcializtion, mark_of_internship):
        
        super().__init__(stu_id, stu_name, stu_age, stu_percentage)
        self.sepcializtion=sepcializtion
        self.mark_of_internship=mark_of_internship
    
    def accept(self):

        super().accept()
        self.sepcializtion=input("ENTER THE MEDICAL SEPCIALIZATION : ")
        self.mark_of_internship=int(input("ENTER THE  MEDICAL MARK OF INTERNSHIP : "))
    
    def CalculateRank(self):
        
        if (self.percentage >=85 and self.mark_of_internship >=80):
            return "Excellent"
        elif(self.percentage >=70 and self.mark_of_internship >=70):
            return "Very Good"
        elif(self.percentage >=50):
            return "Good"
        elif(self.percentage >=35):
            return "Pass"
        else:
            return "Fail"
    
    def display(self):
         
         super().display()
         print("BRANCH : ",self.sepcializtion)
         print("INTERNAL MARKS : ",self.mark_of_internship)
         print("MEDICAL RANK : ",self.CalculateRank())
    
    def __str__(self):

        print("##########################################")
        return (f"STUDENT ID : {self.s_id}\n "
               f"STUDENT NAME : {self.s_name}\n"
               f"STUDENT AGE : {self.age}\n"
               f"STUDENT PERCENTAGE : {self.percentage}\n"
               f"SEPCIALIZTION : {self.sepcializtion}\n"
               f"MARKS OF INTERNSHIP : {self.mark_of_internship}\n"
               f"RANK : {self.CalculateRank()}") 

m1 = Medical(101,'Pratima',32,75,'Gynecologist',70)
m1.display()
print(m1)    